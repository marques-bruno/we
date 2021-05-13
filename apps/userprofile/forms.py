from userauth.models import User
from django import forms
from django.forms import ModelForm


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'birthdate', 'picture']
        widgets = {'birthdate': forms.DateInput(attrs={'type':'date'})}

