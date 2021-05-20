from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View, UpdateView, CreateView, FormView
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.core import serializers

from .forms import AddressForm, BillingForm
from userauth.models import Address
from store.models import Order


class SameUserOnlyMixin(object):

    def has_permissions(self):
        # Assumes that your Ticket model has a foreign key called user.
        return self.get_object().user == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            return HttpResponseForbidden("You do not have permission to access this page")
        return super(SameUserOnlyMixin, self).dispatch(
            request, *args, **kwargs)


class AddressCreateView(CreateView):
    model = Address
    form_class = AddressForm
    success_url = reverse_lazy('sales_pipeline:billing')
    template_name='address.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

address_view = login_required(AddressCreateView.as_view())


class AddressUpdateView(SameUserOnlyMixin, UpdateView):
    model = Address
    form_class = AddressForm
    success_url = reverse_lazy('sales_pipeline:billing')
    template_name='address.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

address_update_view = login_required(AddressUpdateView.as_view())


class BillingView(FormView):
    template_name = 'billing.html'
    form_class = BillingForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FormView, self).get_context_data(**kwargs)
        context['addrs'] = Address.objects.filter(user=context['view'].request.user)
        context['json_addrs'] = serializers.serialize('json', Address.objects.filter(user=context['view'].request.user).all())
        return context
        
    def get_form(self, form_class=None):
        """Return an instance of the form to be used in this view."""
        if form_class is None:
            form_class = self.get_form_class()
        form = form_class(**self.get_form_kwargs())
        if Address.objects.filter(user=self.request.user, is_primary=True).count():
            form.fields['address'].initial = Address.objects.filter(user=self.request.user, is_primary=True)[0]
        form.fields['address'].queryset = Address.objects.filter(user=self.request.user)
        return form

    def post(self, *args, **kwargs):
        form = BillingForm(self.request.POST or None)
        if form.is_valid():
            if self.request.POST.get('submit', '') == 'update_addr':
                messages.warning(self.request, 'updating address')
                return redirect('sales_pipeline:update_address', pk=form.cleaned_data['address'].pk)

            order_qs = Order.objects.filter(user=self.request.user, complete=False)
            if order_qs.exists():
                order = order_qs[0]
                order.address = form.cleaned_data['address']
                order.customer_message = form.cleaned_data['customer_message']
                order.save()
            return redirect('sales_pipeline:payment')
        else:
            print(self.request.POST)            
            messages.warning(self.request, 'oups, something went wrong: invalid form')
            return redirect('/')

billing_view = login_required(BillingView.as_view())
