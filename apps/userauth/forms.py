from .models import CustomUser, CustomerUser, SupplierUser, ManagerUser
from wagtail.users.forms import UserCreationForm, UserEditForm
from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as tr
from allauth.account.forms import SignupForm
from django.core.validators import RegexValidator

class WagtailUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        widgets = {'birthdate': forms.DateInput(attrs={'type':'date'})}


class WagtailUserEditForm(UserEditForm):
    class Meta(UserEditForm.Meta):
        model = CustomUser
        widgets = {'birthdate': forms.DateInput(attrs={'type':'date'})}



class CustomUserUpdateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'birthdate', 'address1', 'address2', 'zip_code', 'city', 'country', 'mobile_phone', 'additional_information', 'picture', 'is_supplier', 'is_manager']
        widgets = {'birthdate': forms.DateInput(attrs={'type':'date'})}


class CustomerSignupForm(SignupForm):
    ## declare here all the extra fields in CustomerUser model WITHOUT
    ## the OneToOneField to User
    ## (N.B: do NOT try to declare Meta class with model=CustomerUser,
    ## it won't work!)
    first_name = forms.CharField(max_length=30, label=tr("First name"))
    last_name = forms.CharField(max_length=30, label=tr("Last name"))

    ## Call SignupForm.__init__ to make sure you get the extra password fields:
    def __init__(self, *args, **kwargs):
        SignupForm.__init__(self, *args, **kwargs)

    def clean(self):
        super(CustomerSignupForm, self).clean()

    ## Override the save method to save the extra fields
    ## (otherwise the form will save the User instance only)
    def save(self, request):
        ## Save the User instance and get a reference to it
        user = super(CustomerSignupForm, self).save(request)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_supplier = False
        user.is_manager = False

        user.save()

        ## Create an instance of your model with the extra fields
        ## then save it.
        ## (N.B: the are already cleaned, but if you want to do some
        ## extra cleaning just override the clean method as usual)
        customer_user = CustomerUser(
            user=user,
            ## Here add your extra fields from the SupplierUser table
            # supplieruser_fields=self.cleaned_data.get('supplieruser_fields')
        )
        customer_user.save()

        # Remember to return the User instance (not your custom user,
        # the Django one), otherwise you will get an error when the
        # complete_signup method will try to look at it.
        return customer_user.user



class SupplierSignupForm(SignupForm):
    ## declare here all the extra fields in SupplierUser model WITHOUT
    ## the OneToOneField to User
    ## (N.B: do NOT try to declare Meta class with model=SupplierUser,
    ## it won't work!) ex:

    first_name = forms.CharField(max_length=30, label=tr("First name"))
    last_name = forms.CharField(max_length=30, label=tr("Last name"))
    # phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=tr("Enter a valid international mobile phone number starting with +(country code)"))
    # mobile_phone = forms.CharField(validators=[phone_regex], label=tr("Mobile phone"), max_length=17)

    def __init__(self, *args, **kwargs):
        SignupForm.__init__(self, *args, **kwargs)

    def clean(self):
        super(SupplierSignupForm, self).clean()

    ## Override the save method to save the extra fields
    ## (otherwise the form will save the User instance only)
    def save(self, request):
        ## Save the User instance and get a reference to it
        user = super(SupplierSignupForm, self).save(request)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        # user.mobile_phone = self.cleaned_data['mobile_phone']
        user.is_supplier = True
        user.is_manager = False
        user.save()

        ## Create an instance of your model with the extra fields
        ## then save it.
        ## (N.B: the are already cleaned, but if you want to do some
        ## extra cleaning just override the clean method as usual)
        supplier_user = SupplierUser(
            user=user,
            ## Here add your extra fields from the SupplierUser table
            # supplieruser_fields=self.cleaned_data.get('supplieruser_fields')
        )
        supplier_user.save()

        # Remember to return the User instance (not your custom user,
        # the Django one), otherwise you will get an error when the
        # complete_signup method will try to look at it.
        return supplier_user.user


class ManagerSignupForm(SignupForm):
    ## declare here all the extra fields in SupplierUser model WITHOUT
    ## the OneToOneField to User
    ## (N.B: do NOT try to declare Meta class with model=SupplierUser,
    ## it won't work!) ex:

    first_name = forms.CharField(max_length=30, label=tr("First name"))
    last_name = forms.CharField(max_length=30, label=tr("Last name"))
    # phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=tr("Enter a valid international mobile phone number starting with +(country code)"))
    # mobile_phone = forms.CharField(validators=[phone_regex], label=tr("Mobile phone"), max_length=17)

    def __init__(self, *args, **kwargs):
        SignupForm.__init__(self, *args, **kwargs)

    def clean(self):
        super(ManagerSignupForm, self).clean()

    ## Override the save method to save the extra fields
    ## (otherwise the form will save the User instance only)
    def save(self, request):
        ## Save the User instance and get a reference to it
        user = super(ManagerSignupForm, self).save(request)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        # user.mobile_phone = self.cleaned_data['mobile_phone']
        user.is_supplier = False
        user.is_manager = True
        user.save()

        ## Create an instance of your model with the extra fields
        ## then save it.
        ## (N.B: the are already cleaned, but if you want to do some
        ## extra cleaning just override the clean method as usual)
        manager_user = ManagerUser(
            user=user,
            ## Here add your extra fields from the SupplierUser table
            # supplieruser_fields=self.cleaned_data.get('supplieruser_fields')
        )
        manager_user.save()

        # Remember to return the User instance (not your custom user,
        # the Django one), otherwise you will get an error when the
        # complete_signup method will try to look at it.
        return manager_user.user

