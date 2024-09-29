from django import forms
# from .models import User

class Login(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)

