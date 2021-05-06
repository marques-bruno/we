from userauth.models import User

from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import View, RedirectView
from django.urls import reverse_lazy
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required
def profile_view(request):
        return redirect('account_dashboard')


@login_required
def account_dashboard_view(request):
    return render(request, 'userprofile/account/account_dashboard.html')


class AccountUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('account_dashboard')
    template_name='userprofile/account/account_update.html'

account_update_view = login_required(AccountUpdateView.as_view())


@login_required
def account_message_board_view(request):
    return render(request, 'userprofile/account/account_message_board.html')


class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('customer_signup')
    template_name='userauth/account/delete.html'

account_delete_view = login_required(AccountDeleteView.as_view())
