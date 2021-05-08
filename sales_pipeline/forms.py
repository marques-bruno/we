from django import forms

from userauth.models import Address


class BillingForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['first_name','last_name','address1','address2','country','city','zip_code']