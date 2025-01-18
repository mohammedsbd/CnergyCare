from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User 

class UserRegistrationForm(UserCreationForm):
  full_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "jhon doe"}))
  email=forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "jhondoe@gmail.com"}))
  password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',"placeholder": "**********"}))
  password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',"placeholder": "**********"}))
  
  class Meta:
      model=User
      fields=['full_name','email','password1','password2','user_type']
      
      
      
class LoginForm(forms.Form):
  email=forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "jhondoe@gmail.com"}))
  password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',"placeholder": "**********"}))
  
  
  class Meta:
      model=User
      fields=['email','password']