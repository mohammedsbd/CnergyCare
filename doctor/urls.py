from django.urls import path
from doctor import views

app_name="doctor"

urlpatterns =[
    path("", views.dashboard, name="dashboard"),
    path("appointments/", views.appointments, name="appointments"),
    path("appointments/<appointment_id>", views.appointment_detail, name="appointment_detail"),
    path("cancel_appointment/<appointment_id>", views.cancel_appointment, name="cancel_appointment"),
    path("activate_appointment/<appointment_id>", views.activate_appointment, name="activate_appointment"),
    path("complete_appointment/<appointment_id>", views.complete_appointment, name="complete_appointment"),
    path("add_medical_report/<appointment_id>", views.add_medical_report, name="add_medical_report"),
    path("edit_medical_report/<appointment_id>/<medical_report_id>/", views.edit_medical_report, name="edit_medical_report"),

]