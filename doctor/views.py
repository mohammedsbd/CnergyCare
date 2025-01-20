from django.shortcuts import render, redirect
from doctor import models as doctor_models
from base import models as base_models
from django.contrib import messages

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointments = base_models.Appointment.objects.filter(doctor=doctor)
    notifications = doctor_models.Notification.objects.filter(doctor=doctor)

    context = {
        "appointments": appointments,
        "notifications": notifications,
    }

    return render(request, "doctor/dashboard.html", context)

@login_required
def appointments(request):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointments = base_models.Appointment.objects.filter(doctor=doctor)

    context = {
        "appointments": appointments,
    }

    return render(request, "doctor/appointments.html", context)

@login_required
def appointment_detail(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)
    
    medical_records = base_models.MedicalRecord.objects.filter(appointment=appointment)
    lab_tests = base_models.LabTest.objects.filter(appointment=appointment)
    prescriptions = base_models.Prescription.objects.filter(appointment=appointment)

    context = {
        "appointment": appointment,
        "medical_records": medical_records,
        "lab_tests": lab_tests,
        "prescriptions": prescriptions,
    }

    return render(request, "doctor/appointment_detail.html", context)




@login_required
def cancel_appointment(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)

    appointment.status = "Cancelled"
    appointment.save()

    messages.success(request, "Appointment Cancelled Successfully")
    return redirect("doctor:appointment_detail", appointment.appointment_id)


@login_required
def activate_appointment(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)

    appointment.status = "Scheduled"
    appointment.save()

    messages.success(request, "Appointment Re-Scheduled Successfully")
    return redirect("doctor:appointment_detail", appointment.appointment_id)


@login_required
def complete_appointment(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)

    appointment.status = "Completed"
    appointment.save()

    messages.success(request, "Appointment Completed Successfully")
    return redirect("doctor:appointment_detail", appointment.appointment_id)



@login_required
def add_medical_report(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)

    if request.method == "POST":
        diagnosis = request.POST.get("diagnosis")
        treatment = request.POST.get("treatment")
        base_models.MedicalRecord.objects.create(appointment=appointment, diagnosis=diagnosis, treatment=treatment)

    
    messages.success(request, "Medical Report Added Successfully")
    return redirect("doctor:appointment_detail", appointment.appointment_id)



@login_required
def edit_medical_report(request, appointment_id, medical_report_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)
    medical_report = base_models.MedicalRecord.objects.get(id=medical_report_id, appointment=appointment)

    if request.method == "POST":
        diagnosis = request.POST.get("diagnosis")
        treatment = request.POST.get("treatment")

        medical_report.diagnosis = diagnosis
        medical_report.treatment = treatment
        medical_report.save()

    messages.success(request, "Medical Report Updated Successfully")
    return redirect("doctor:appointment_detail", appointment.appointment_id)
