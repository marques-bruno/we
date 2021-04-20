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

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.save()


class SupplierSignupForm(SignupForm):
    username = forms.CharField(max_length=30, label=tr("User name"), help_text=tr("Will be shown e.g. when commenting."))
    email = forms.EmailField(label=tr("Email address"))
    def save(self, request):
        user = super(SupplierSignupForm, self).save(request)
        user.is_supplier = True
        user.save()
        return user

class ManagerSignupForm(SignupForm):
    username = forms.CharField(max_length=30, label=tr("User name"), help_text=tr("Will be shown e.g. when commenting."))
    email = forms.EmailField(label=tr("Email address"))
    def save(self, request):
        user = super(ManagerSignupForm, self).save(request)
        user.is_manager = True
        user.save()
        return user


class CustomUserUpdateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'birthdate', 'address1', 'address2', 'zip_code', 'city', 'country', 'mobile_phone', 'additional_information', 'picture', 'is_supplier', 'is_manager']
        widgets = {'birthdate': forms.DateInput(attrs={'type':'date'})}