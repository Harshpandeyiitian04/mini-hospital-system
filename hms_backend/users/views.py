from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import DoctorSignupForm, PatientSignupForm
from .models import User, Patient
from doctors.models import Doctor
from django.contrib.auth.forms import AuthenticationForm
from .google_auth import get_google_flow
from hms_backend.email_service import send_email

def doctor_signup(request):
    if request.method == 'POST':
        form =DoctorSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'doctor'
            user.save()
            Doctor.objects.create(user=user)
            send_email(
                action="SIGNUP_WELCOME",
                email=user.email,
                name=user.username
            )
            login(request,user)
            return redirect('doctor_dashboard')
        else:
            print(form.errors)
    else:
        form=DoctorSignupForm()

    return render(request,'users/signup.html',{'form':form})

def patient_signup(request):
    if request.method == 'POST':
        form =PatientSignupForm(request.POST)
        if form.is_valid():
            user =form.save(commit=False)
            user.role ='patient'
            user.save()
            phone =form.cleaned_data.get('phone')
            Patient.objects.create(
                user=user,
                phone=phone,
            )
            send_email(
                action="SIGNUP_WELCOME",
                email=user.email,
                name=user.username
            )
            login(request,user)
            return redirect('patient_dashboard')
        else:
            print(form.errors)
    else:
        form = PatientSignupForm()

    return render(request,'users/signup.html',{'form':form})

def User_login(request):
    if request.method == 'POST':
        form =AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username =form.cleaned_data.get('username')
            password =form.cleaned_data.get('password')
            user =authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                if user.role == 'doctor':
                    return redirect('doctor_dashboard')
                else:
                    return redirect('patient_dashboard')
    else:
        form =AuthenticationForm()

    return render(request,'users/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')

def google_connect(request):
    flow=get_google_flow()
    auth_url, state = flow.authorization_url()
    request.session['state']=state
    return redirect(auth_url)

def google_callback(request):
    flow = get_google_flow()
    flow.fetch_token(authorization_response=request.build_absolute_uri())
    credentials = flow.credentials
    token_data = {
        "token": credentials.token,
        "refresh_token": credentials.refresh_token,
        "token_uri": credentials.token_uri,
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
        "scopes": credentials.scopes
    }
    user = request.user
    if user.role == 'doctor':
        doctor = Doctor.objects.get(user=user)
        doctor.google_calendar_token = token_data
        doctor.save()
    else:
        patient = Patient.objects.get(user=user)
        patient.google_calendar_token = token_data
        patient.save()
    return redirect('/')