from django.urls import path
from patient import views

app_name="patient"

urlpatterns =[
    path("", views.dashboard, name="dashboard"),
   

]