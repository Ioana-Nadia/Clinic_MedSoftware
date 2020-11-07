from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from .models import Clinic

class registerForm(UserCreationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'nameClass inputClass', 'placeholder':'Name of the clinic'}))
    email = forms.EmailField(max_length=60, widget=forms.EmailInput(attrs={'class':'emailClass inputClass', 'placeholder':'Email'}))
    address = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'addressClass inputClass', 'placeholder':'Address'}))
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class':'psw1Class inputClass', 'placeholder':'Password'}))
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class':'psw2Class inputClass', 'placeholder':'Confirm password'}))
    class Meta:
         model = Clinic
         fields = ('username', 'email', 'address', 'password1', 'password2', )

# class displayForm(forms.ModelForm):
#     class Meta:
#         model = Patient
#         fields = '__all__'
