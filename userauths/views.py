from django.shortcuts import render, redirect
from django.contrib import messages
from userauths import forms as userauths_forms

# Create your views here.

def Register_view(request):
    if request.user.is_authenticated:
        messages.success(request,"You are already logged in")
        return redirect('/')
    form=userauths_forms.UserRegistrationForm(request.POST or None)
    
    if form.is_valid():
       user= form.save()
       full_name=form.cleaned_data.get("full_name")
       email=form.cleaned_data.get("email")
       password=form.cleaned_data.get("password")
        
        
    context={
        "form": form
    }
    return render(request,"userauths/sign-up.html",context)
