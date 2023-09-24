from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
class SignupForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']  
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists.')
        return email
    
    def clean_password(self):
        password = self.cleaned_data['password']

        # Check if the password contains at least one lowercase letter
        if not re.search(r'[a-z]', password):
            raise forms.ValidationError('Password must contain at least one lowercase letter.')

        # Check if the password contains at least one uppercase letter
        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError('Password must contain at least one uppercase letter.')

        # Check if the password contains at least one digit
        if not re.search(r'[0-9]', password):
            raise forms.ValidationError('Password must contain at least one digit.')

        # Check if the password contains at least one special character
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise forms.ValidationError('Password must contain at least one special character.')

        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password') 
        confirm_password = cleaned_data.get('confirm_password')  

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Password and confirm password do not match.')

        return cleaned_data
