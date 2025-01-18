from django.urls import paths
from userauths import views

app_name="userauths"

urlpatterns =[  
    path("sign-up/",views.register_view,name="sign-up")
]