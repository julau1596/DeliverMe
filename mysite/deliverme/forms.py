from django import forms
from django.contrib.auth.forms import UserCreationForm
from deliverme.models import User

from django.core.validators import RegexValidator

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='')
    last_name = forms.CharField(max_length=30, required=False, help_text='')
    
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = forms.CharField(validators=[phone_regex], max_length=17) # validators should be a list
    
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number' , 'password1', 'password2', )