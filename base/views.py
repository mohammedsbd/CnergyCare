from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from base import models as base_models
from doctor import models as doctor_models
from patient import models as patient_models

def index(request):
    services = base_models.Service.objects.all()
    
    context = {
        "services": services
    }
    return render(request, 'base/index.html', context)

def service_detail(request, service_id):
    service = base_models.Service.objects.get(id=service_id)
    
    context = {
        "service": service
    }
    return render(request, 'base/service_detail.html', context)


@login_required
def book_appointment(request, service_id, doctor_id):
    service=base_models.Service.objects.get(id=service_id)
    doctor=doctor_models.Doctor.objects.get(id=doctor_id)
    patient=patient_models.Patient.objects.get(user=request.user)
    
    if request.method == 'POST':
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        gender = request.POST.get("gender")
        address = request.POST.get("address")
        dob = request.POST.get("dob")
        issues = request.POST.get("issues")
        symptoms = request.POST.get("symptoms")
        
        # Update patient bio data
        patient.full_name = full_name
        patient.email = email
        patient.mobile = mobile
        patient.gender = gender
        patient.address = address
        patient.dob = dob
        patient.save()
        
        # Create appointment object
        appointment = base_models.Appointment.objects.create(
            service=service,
            doctor=doctor,
            patient=patient,
            appointment_date=doctor.next_available_appointment_date,
            issues=issues,
            symptoms=symptoms,
        )
        
        # Create a billing objects
        billing = base_models.Billing()
        billing.patient = patient
        billing.appointment = appointment
        billing.sub_total = appointment.service.cost
        billing.tax = appointment.service.cost * 5 / 100
        billing.total = billing.sub_total + billing.tax
        billing.status = "Unpaid"
        # billing.save()

        return redirect("base:checkout", billing.billing_id)


        
        
        
        
        
    context = {
        "service": service,
        "doctor": doctor,
        "patient": patient
    }
    return render(request, 'base/book_appointment.html', context)
