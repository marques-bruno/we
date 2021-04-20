from .models import CustomUser
from .forms import SupplierSignupForm
from .forms import ManagerSignupForm

from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CustomUserUpdateForm
from django.contrib.auth.decorators import login_required

from allauth.account.views import SignupView

@login_required
def profile_view(request):
    return render(request, 'account/profile.html')


class CustomUserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    success_url = reverse_lazy('account_profile')


class CustomUserDeleteView(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('account_signup')


class SupplierUserRegistrationView(SignupView):
    form_class = SupplierSignupForm
    redirect_field_name = 'next'
    view_name = 'signup-supplier'
    success_url = None

    def get_context_data(self, **kwargs):
        ret = super(SupplierUserRegistrationView, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret


class ManagerUserRegistrationView(SignupView):
    form_class = ManagerSignupForm
    redirect_field_name = 'next'
    view_name = 'signup-manager'
    success_url = None

    def get_context_data(self, **kwargs):
        ret = super(ManagerUserRegistrationView, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret


# suppliersignup = SupplierUserRegistrationView.as_view()
# managersignup = ManagerUserRegistrationView.as_view()