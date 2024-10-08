from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'field-input'}),label='Создайте имя пользователя',)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'field-input'}),label='Создайте электронную почту')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'field-input'}),label='Придумайте пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'field-input'}),label='Повторите пароль')


    class Meta:
        model = User
        fields = ['username','email','password1']



class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'field-input'}),label='Введите имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'field-input'}),label='Введите пароль')


    class Meta:
        model = User
        fields = ['username','password']
