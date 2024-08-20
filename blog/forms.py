from django.forms import forms
from .models import *
from django.forms import ModelForm,TextInput,Textarea,EmailInput
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class DetailForm(ModelForm):
    class Meta:
        model = Zakaz
        fields = ["username","phonenumber","carname"]
        widgets = {
            "username":TextInput(attrs={
            "class":"i",
            "placeholder" : "Ваш имя",  
            }),
            "phonenumber":TextInput(attrs={
            "class":"i",
            "placeholder" : "Ваш телефон"
            }),
            "carname":TextInput(attrs={
            "class":"i",
            "placeholder" : "Имя машины",
            }),
        }   