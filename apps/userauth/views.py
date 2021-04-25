from .forms import CustomerSignupForm, SupplierSignupForm, ManagerSignupForm
from allauth.account.views import SignupView

class CustomerUserSignupView(SignupView):
    # The referenced HTML content can be copied from the signup.html
    # in the django-allauth template folder
    template_name = 'account/signup.html'
    # the previously created form class
    form_class = CustomerSignupForm

    # I don't use them, but you could override them
    # (N.B: the following values are the default)
    # success_url = None
    # redirect_field_name = 'next'

# # Create the view (we will reference to it in the url patterns)
customer_signup = CustomerUserSignupView.as_view()


class SupplierUserSignupView(SignupView):
    # The referenced HTML content can be copied from the signup.html
    # in the django-allauth template folder
    template_name = 'account/signup_supplier.html'
    # the previously created form class
    form_class = SupplierSignupForm

    # I don't use them, but you could override them
    # (N.B: the following values are the default)
    # success_url = None
    # redirect_field_name = 'next'

# # Create the view (we will reference to it in the url patterns)
supplier_signup = SupplierUserSignupView.as_view()


class ManagerUserSignupView(SignupView):
    # The referenced HTML content can be copied from the signup.html
    # in the django-allauth template folder
    template_name = 'account/signup_manager.html'
    # the previously created form class
    form_class = ManagerSignupForm

    # I don't use them, but you could override them
    # (N.B: the following values are the default)
    # success_url = None
    # redirect_field_name = 'next'

# # Create the view (we will reference to it in the url patterns)
manager_signup = ManagerUserSignupView.as_view()