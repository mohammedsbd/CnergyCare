

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
