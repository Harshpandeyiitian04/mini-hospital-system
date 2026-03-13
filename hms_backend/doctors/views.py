from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Doctor, AvailabilitySlot
from .forms import AvailabilityForm

@login_required
def doctor_dashboard(request):
    if request.user.role != 'doctor':
        return redirect('login')
    doctor = Doctor.objects.get(user=request.user)
    slots =AvailabilitySlot.objects.filter(doctor=doctor).order_by('date','start_time')
    return render(request,'doctors/dashboard.html',{
        'slots':slots
    })

@login_required
def create_slot(request):
    if request.user.role != 'doctor':
        return redirect('login')
    doctor =Doctor.objects.get(user=request.user)
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            slot =form.save(commit=False)
            slot.doctor =doctor
            slot.save()
            return redirect('doctor_dashboard')
        else:
            print(form.errors)
    else:
        form=AvailabilityForm()
    return render(request,'doctors/create_slot.html',{
        'form':form
    })