from django.urls import path
from . import views

urlpatterns =[
    path('dashboard/',views.doctor_dashboard,name='doctor_dashboard'),
    path('create-slot/',views.create_slot,name='create_slot'),
]