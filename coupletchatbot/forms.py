from django import forms
from django.forms.formsets import MAX_NUM_FORM_COUNT

class LoginForm(forms.Form):
    email = forms.EmailField(label='email', max_length=48, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='password', max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form):
    email = forms.EmailField(label='email', max_length=48, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='username', max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='password', max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='comfirm_password', max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control'}))