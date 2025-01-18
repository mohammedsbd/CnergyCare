from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate ,login, logout
from userauths import forms as userauths_forms
from doctor import models as doctor_models
from patient import models as patient_models

# Create your views here.

def Register_view(request):
    if request.user.is_authenticated:
        messages.success(request,"You are already logged in")
        return redirect('/')
    
    
    if request.method == 'POST':
        form=userauths_forms.UserRegistrationForm(request.POST or None)
    
        if form.is_valid():
           user= form.save()
           full_name=form.cleaned_data.get("full_name")
           email = form.cleaned_data.get("email")
           password1=form.cleaned_data.get("password1")
           user_type=form.cleaned_data.get("user_type")
       
       
       
       
    #    to immidetly login the user without taking time
           user=authenticate(request,email=email, password=password1)
           print("user type =======" ,user_type)
           if user is not None:
              login(request,user)
           
           
           if user_type=="Doctor":
               doctor_models.Doctor.objects.create(user=user, full_name=full_name)
           else:
               patient_models.Patient.objects.create(user=user, full_name=full_name, email=email)
   
    
           messages.success(request,"Account Created Successfully")
           return redirect('/')
    
    else:
            messages.error(request,"Authentication Failed, please try again")
        
    
    context={
        "form": form
    }
    return render(request,"userauths/sign-up.html",context)



def login_view(request):
    if request.user.is_authenticated:
        messages.success(request,"You are already logged in")
        return redirect('/')
    
    if request.method =="POST":
        form=userauths_forms.LoginForm(request.POST or None)
