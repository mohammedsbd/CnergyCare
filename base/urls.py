from django.urls import path
from base import views

app_name="base"

urlpatterns =[
    path("", views.index, name="index"),
    path("service/<service_id>/", views.service_detail, name="service_detail"),
]