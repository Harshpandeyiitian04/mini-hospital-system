from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class DoctorSignupForm(UserCreationForm):
    email =forms.EmailField()
    
    class Meta:
        model =User
        fields =['username','email','password1','password2']

class PatientSignupForm(UserCreationForm):
    email =forms.EmailField()
    phone =forms.CharField(max_length=15)

    class Meta:
        model =User
        fields =['username','email','password1','password2']