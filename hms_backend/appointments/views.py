from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from doctors.models import Doctor, AvailabilitySlot
from users.models import Patient
from .models import Appointment
from django.db import transaction
from hms_backend.google_calendar import create_calendar_event
from hms_backend.email_service import send_email

@login_required
def patient_dashboard(request):
    if request.user.role != 'patient':
        return redirect('login')
    doctors = Doctor.objects.all()
    return render(request,'appointments/patient_dashboard.html',{
        'doctors':doctors
    })

@login_required
def doctor_slots(request,doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    slots = AvailabilitySlot.objects.filter(
        doctor=doctor,
        is_booked=False
    ).order_by('date','start_time')
    return render(request,'appointments/doctor_slots.html',{
        'doctor':doctor,
        'slots':slots
    })

@login_required
def book_slot(request,slot_id):
    if request.user.role != 'patient':
        return redirect('login')
    patient = Patient.objects.get(user=request.user)
    try:
        with transaction.atomic():
            slot = AvailabilitySlot.objects.select_for_update().get(
                id=slot_id,
                is_booked=False
            )
            if slot.is_booked:
                return render(request,'appointments/error.html',{
                    'message':'This slot has already been booked.'
                })
            Appointment.objects.create(
                patient=patient,
                slot=slot
            )
            slot.is_booked = True
            slot.save()
            doctor = slot.doctor
            doctor_token = doctor.google_calendar_token
            patient_token = patient.google_calendar_token
            start = f"{slot.date}T{slot.start_time}:00"
            end = f"{slot.date}T{slot.end_time}:00"
            summary = f"Appointment with Dr {doctor.user.username}"
            try:
                if doctor_token:
                    create_calendar_event(doctor_token, summary, start, end)
                if patient_token:
                    create_calendar_event(patient_token, summary, start, end)
            except Exception as e:
                print("Calendar event creation failed:", e)
            doctor_name = slot.doctor.user.username
            time = f"{slot.date} {slot.start_time}"
            send_email(
                action="BOOKING_CONFIRMATION",
                email=request.user.email,
                name=request.user.username,
                doctor=doctor_name,
                time=time
            )
    except AvailabilitySlot.DoesNotExist:
        return redirect('patient_dashboard')
    return redirect('patient_dashboard')