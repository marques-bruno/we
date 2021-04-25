from .models import CustomUser

from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CustomUserUpdateForm, CustomerSignupForm, SupplierSignupForm, ManagerSignupForm
from django.contrib.auth.decorators import login_required

from allauth.account.views import SignupView

@login_required
def profile_view(request):
    # return render(request, 'account/profile.html')
    return render(request, 'account/profile_supplier.html', {'model': CustomUser, 'form': CustomUserUpdateForm, 'success_url': reverse_lazy('account_profile')})

@login_required
def supplier_profile_view(request):
    return render(request, 'account/profile_supplier.html')


class CustomUserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    success_url = reverse_lazy('account_profile')


class CustomUserDeleteView(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('account_signup')



class CustomerUserSignupView(SignupView):
    # The referenced HTML content can be copied from the signup.html
    # in the django-allauth template folder
    template_name = 'account/signup.html'
    # the previously created form class
    form_class = CustomerSignupForm

    # the view is created just a few lines below
    # N.B: use the same name or it will blow up
    view_name = 'customer_signup'

    # I don't use them, but you could override them
    # (N.B: the following values are the default)
    # success_url = None
    # redirect_field_name = 'next'

# # Create the view (we will reference to it in the url patterns)
# customer_signup = CustomerUserSignupView.as_view()


class SupplierUserSignupView(SignupView):
    # The referenced HTML content can be copied from the signup.html
    # in the django-allauth template folder
    template_name = 'account/signup_supplier.html'
    # the previously created form class
    form_class = SupplierSignupForm

    # the view is created just a few lines below
    # N.B: use the same name or it will blow up
    view_name = 'supplier_signup'

    # I don't use them, but you could override them
    # (N.B: the following values are the default)
    # success_url = None
    # redirect_field_name = 'next'

# # Create the view (we will reference to it in the url patterns)
# supplier_signup = SupplierUserSignupView.as_view()


class ManagerUserSignupView(SignupView):
    # The referenced HTML content can be copied from the signup.html
    # in the django-allauth template folder
    template_name = 'account/signup_manager.html'
    # the previously created form class
    form_class = ManagerSignupForm

    # the view is created just a few lines below
    # N.B: use the same name or it will blow up
    view_name = 'manager_signup'

    # I don't use them, but you could override them
    # (N.B: the following values are the default)
    # success_url = None
    # redirect_field_name = 'next'

# # Create the view (we will reference to it in the url patterns)
# supplier_signup = SupplierUserSignupView.as_view()