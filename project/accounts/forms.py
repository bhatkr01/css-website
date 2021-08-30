from django.forms import ModelForm,TextInput, DateInput
from django.forms.widgets import PasswordInput
from accounts.models import MyUser
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):

    class Meta:
        model = MyUser
        password1= forms.CharField(label='Password')
        password2= forms.CharField(label='Repeat Password')
        fields = ('email', 'date_of_birth', 'first_name', 'last_name', 'year')
        widgets = {
            'email': TextInput(attrs={'placeholder': '*****@abc.com'}),
            'date_of_birth': DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'first_name': TextInput(attrs={'placeholder': 'Your Name'}),
            'last_name': TextInput(attrs={'placeholder': 'Your last Name'}),
            'password1':PasswordInput,
            'password2':PasswordInput,
        }

    