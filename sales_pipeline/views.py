from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from .forms import BillingForm


class BillingView(View):
    def get(self, *args, **kwargs):
        ctx = {'form': BillingForm()}
        return render(self.request, 'billing.html', ctx)

    def post(self, *args, **kwargs):
        form = BillingForm(self.request.POST or None)
        if form.is_valid():
            print(" the form is valid ")
            return redirect('sales_pipeline:billing')
        return 

billing_view = login_required(BillingView.as_view())