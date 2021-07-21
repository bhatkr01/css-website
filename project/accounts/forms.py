from django.forms import ModelForm,TextInput, DateInput
from accounts.models import MyUser

class SignUpForm(ModelForm):

    class Meta:
        model = MyUser
        fields = ('email', 'date_of_birth', 'first_name', 'last_name', 'year')
        widgets = {
            'email': TextInput(attrs={'placeholder': '*****@abc.com'}),
            'date_of_birth': DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'first_name': TextInput(attrs={'placeholder': 'Your Name'}),
            'last_name': TextInput(attrs={'placeholder': 'Your last Name'}),
        }

    