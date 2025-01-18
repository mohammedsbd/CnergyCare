from django.shortcuts import render, redirect
from django.contrib import messages
from userauths import forms as userauths_forms

# Create your views here.

def Register_view(request):
    if request.user.is_authenticated:
        messages.success(request,"You are already logged in")
        return redirect('/')
    form=userauths_forms.UserRegistrationForm()
    context={
        "form": form
    }
    return render(request,"userauths/signup.html",context)
