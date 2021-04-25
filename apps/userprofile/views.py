from userauth.models import User

from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'dashboard.html', {
        'tab': 'dashboard',
    })


@login_required
def supplier_profile_view(request):
    return render(request, 'userprofile/account/profile_supplier.html')


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('account_profile')
    template_name='account/update.html'

user_update_view = UserUpdateView.as_view()


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('account_signup')
    template_name='account/delete.html'

user_delete_view = UserDeleteView.as_view()
