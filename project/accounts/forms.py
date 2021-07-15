from django.forms import ModelForm,TextInput, DateInput
from accounts.models import MyUser

class SignUpForm(ModelForm):

    class Meta:
        model = MyUser
        fields = ('email', 'date_of_birth', 'first_name', 'last_name', 'year')
        widgets = {
            'date_of_birth': DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }

    