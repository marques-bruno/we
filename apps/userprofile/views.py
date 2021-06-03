from userauth.models import User, SupplierUser

from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import View, RedirectView
from django.urls import reverse_lazy
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from store.models import Product

@login_required
def profile_view(request):
        return redirect('account_dashboard', pk=request.user.pk)


@login_required
def account_dashboard_view(request, pk=0):
    return render(request, 'userprofile/account/account_dashboard.html')


class AccountUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('account_dashboard')
    template_name='userprofile/account/account_update.html'

account_update_view = login_required(AccountUpdateView.as_view())


@login_required
def account_message_board_view(request, pk=0):
    return render(request, 'userprofile/account/account_message_board.html')


class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('customer_signup')
    template_name='userauth/account/delete.html'

account_delete_view = login_required(AccountDeleteView.as_view())


@login_required
def account_sales_view(request, pk=0):
    return render(request, 'userprofile/account/account_sales.html')


@login_required
def account_products_view(request, pk=0):
    context = {
        'products': Product.objects.filter(supplier=SupplierUser.objects.filter(user=request.user)[0])
    }
    return render(request, 'userprofile/account/account_products.html', context)


@login_required
def account_calendar_view(request, pk=0):
    return render(request, 'userprofile/account/account_calendar.html')


@login_required
def account_documents_view(request, pk=0):
    return render(request, 'userprofile/account/account_documents.html')


