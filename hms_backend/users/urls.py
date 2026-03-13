from django.urls import path
from . import views

urlpatterns =[
    path('signup/doctor/',views.doctor_signup,name='doctor_signup'),
    path('signup/patient/',views.patient_signup,name='patient_signup'),

    path('login/',views.User_login,name='login'),
    path('logout/',views.user_logout,name='logout'),

    path('google/connect/',views.google_connect,name='google_connect'),
    path('oauth/callback/',views.google_callback,name='google_callback'),
    
]