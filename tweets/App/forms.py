from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForms(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['text','photo']
        
class UserRegistrationForms(UserCreationForm):
    email=forms.EmailField()
    class  Meta:
        model=User
        fields=('username','email','password1','password2')
       