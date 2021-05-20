from .forms import CustomerSignupForm, SupplierSignupForm, ManagerSignupForm
from allauth.account.views import SignupView


###################### REST FRAMEWORK ModelView sets ######################


from rest_framework import viewsets
from .serializers import AddressSerializer, CustomerSerializer, ManagerSerializer, SupplierSerializer, UserSerializer
from .models import Address, CustomerUser, ManagerUser, SupplierUser, User


class AddressView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = CustomerUser.objects.all()

class SupplierView(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = SupplierUser.objects.all()

class ManagerView(viewsets.ModelViewSet):
    serializer_class = ManagerSerializer
    queryset = ManagerUser.objects.all()

###########################################################################



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
    template_name = 'account/supplier_signup.html'
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
    template_name = 'account/manager_signup.html'
    # the previously created form class
    form_class = ManagerSignupForm

    # I don't use them, but you could override them
    # (N.B: the following values are the default)
    # success_url = None
    # redirect_field_name = 'next'

# # Create the view (we will reference to it in the url patterns)
manager_signup = ManagerUserSignupView.as_view()

