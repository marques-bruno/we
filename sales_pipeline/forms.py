from django import forms
from django.utils.translation import gettext_lazy as tr

from userauth.models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'first_name','last_name','address1','address2','country','city','zip_code', 'additional_information', 'is_primary']



class BillingForm(forms.Form):
    address = forms.ModelChoiceField(
        help_text=tr('Choose your billing address'), 
        queryset=Address.objects.all(), initial=0)
    customer_message = forms.CharField(
        required=False,
        help_text=tr('Do you want to leave us a message about your order?'), 
        widget=forms.Textarea(attrs={"rows":5, "cols":80})
    )

    # def __init__(self, *args, **kwargs):
    #     addr_qs = kwargs.get('queryset')
    #     kwargs.pop('queryset')
    #     super(forms.Form, self).__init__(*args, **kwargs)
    #     initial_set = False
    #     self.address = forms.ModelChoiceField(queryset=addr_qs)
    #     self.address.queryset
    #     i = 0
    #     for addr in addr_qs:
    #         if addr.is_primary:
    #             self.address.initial={str(i): addr}
    #             break
    #         i+=1
