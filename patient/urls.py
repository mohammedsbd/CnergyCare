from django.urls import path
from patient import views

app_name="patient"

urlpatterns =[
    path("", views.dashboard, name="dashboard"),
    path("appointments", views.appointments, name="appointments"),
    path("appointment_detail/<appointment_id>", views.appointment_detail, name="appointment_detail"),
   

]