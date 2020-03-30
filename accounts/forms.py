from django import forms
from django.contrib.auth.models import User
from .models import Profile



class UserUpdateForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    

    class Meta:
        model = User
        fields = ['username','email']
        

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['image','phone']
