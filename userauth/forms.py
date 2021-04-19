from .models import CustomUser
from wagtail.users.forms import UserCreationForm, UserEditForm
from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as tr

class WagtailUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        widgets = {'birthdate': forms.DateInput(attrs={'type':'date'})}


class WagtailUserEditForm(UserEditForm):
    class Meta(UserEditForm.Meta):
        model = CustomUser
        widgets = {'birthdate': forms.DateInput(attrs={'type':'date'})}


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label=tr("First name"))
    last_name = forms.CharField(max_length=30, label=tr("Last name"))
    username = forms.CharField(max_length=30, label=tr("User name"), help_text=tr("Will be shown e.g. when commenting."))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.save()


class CustomUserUpdateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'birthdate', 'address1', 'address2', 'zip_code', 'city', 'country', 'mobile_phone', 'additional_information', 'picture',]
        widgets = {'birthdate': forms.DateInput(attrs={'type':'date'})}