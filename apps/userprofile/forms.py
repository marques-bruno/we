from userauth.models import User
from django import forms
from django.forms import ModelForm


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'birthdate', 'address1', 'address2', 'zip_code', 'city', 'country', 'mobile_phone', 'additional_information', 'picture', 'is_supplier', 'is_manager']
        widgets = {'birthdate': forms.DateInput(attrs={'type':'date'})}
