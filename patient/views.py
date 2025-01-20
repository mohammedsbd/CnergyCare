

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models

from base import models as base_models
from patient import models as patient_models



@login_required
def dashboard(request):
    patient = patient_models.Patient.objects.get(user=request.user)
    appointments = base_models.Appointment.objects.filter(patient=patient)
    notifications = patient_models.Notification.objects.filter(patient=patient, seen=False)
    total_spent = base_models.Billing.objects.filter(patient=patient).aggregate(total_spent = models.Sum("total"))['total_spent']
    
    context = {
        'appointments': appointments,
        'notifications': notifications,
        'total_spent': total_spent,
    }

    return render(request, "patient/dashboard.html", context)



@login_required
def appointments(request):
    patient = patient_models.Patient.objects.get(user=request.user)
    appointments = base_models.Appointment.objects.filter(patient=patient)

    context = {
        "appointments": appointments,
    }

    return render(request, "patient/appointments.html", context)



@login_required
def appointment_detail(request, appointment_id):
    patient = patient_models.Patient.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, patient=patient)
    
    medical_records = base_models.MedicalRecord.objects.filter(appointment=appointment)
    lab_tests = base_models.LabTest.objects.filter(appointment=appointment)
    prescriptions = base_models.Prescription.objects.filter(appointment=appointment)

    context = {
        "appointment": appointment,
        "medical_records": medical_records,
        "lab_tests": lab_tests,
        "prescriptions": prescriptions,
    }

    return render(request, "patient/appointment_detail.html", context)



@login_required
def cancel_appointment(request, appointment_id):
    patient = patient_models.Patient.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, patient=patient)

    appointment.status = "Cancelled"
    appointment.save()

    messages.success(request, "Appointment Cancelled Successfully")
    return redirect("patient:appointment_detail", appointment.appointment_id)


@login_required
def activate_appointment(request, appointment_id):
    patient = patient_models.Patient.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, patient=patient)

    appointment.status = "Scheduled"
    appointment.save()

    messages.success(request, "Appointment Re-Scheduled Successfully")
    return redirect("patient:appointment_detail", appointment.appointment_id)


@login_required
def complete_appointment(request, appointment_id):
    patient = patient_models.Patient.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, patient=patient)

    appointment.status = "Completed"
    appointment.save()

    messages.success(request, "Appointment Completed Successfully")
    return redirect("patient:appointment_detail", appointment.appointment_id)
