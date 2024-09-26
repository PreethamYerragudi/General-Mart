from django import forms
from .models import User

class Login(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'