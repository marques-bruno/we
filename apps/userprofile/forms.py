from userauth.models import User
from django import forms
from django.forms import ModelForm


class UserUpdateForm(ModelForm):
    class Meta:
        user = User
        fields = ['username', 'email', 'birthdate', 'picture', 'address', 'is_supplier', 'is_manager']
        widgets = {'birthdate': forms.DateInput(attrs={'type':'date'})}

