from django.urls import path
from doctor import views

app_name="doctor"

urlpatterns =[
    path("", views.dashboard, name="dashboard"),

]