from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.views.generic import View, DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .store_models import Product, OrderItem, Order
from userauth.models import User


def product_list_view(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, "product_list.html", context)


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"

product_detail_view = ProductDetailView.as_view()

def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, complete=False)
    if order_qs.exists():
        order = order_qs[0]
        # Get the OrderItem(s) referencing this order and product
        order_items = OrderItem.objects.filter(order=order, product=item)
        if order_items.exists():
            # order_items[0].quantity += request.quantity
            existing_order_item = order_items[0]
            existing_order_item.quantity += 1
            existing_order_item.save()
            messages.info(request, 'Your cart has been updated')
        else:
            # order_item = OrderItem.objects.create(product=item, order=order, quantity=request.quantity)
            order_item = OrderItem.objects.create(product=item, order=order, quantity=1)
            order_item.save()
            messages.info(request, item.name + 'x' + str(order_item.quantity) + ' has been added to your cart')
    else:
        order = Order.objects.create(user=request.user)
        order.save()
        # order_item = OrderItem.objects.create(product=item, order=order, quantity=request.quantity)
        order_item = OrderItem.objects.create(product=item, order=order, quantity=1)
        order_item.save()
        messages.info(request, item.name + 'x' + str(order_item.quantity) + ' has been added to your cart')
    return

@login_required
def add_to_cart_view(request, slug):
    add_to_cart(request, slug)
    return redirect("store:product", slug=slug)

@login_required
def add_single_item_from_cart_view(request, slug):
    add_to_cart(request, slug)
    return redirect("store:order_summary")

# @todo: remove later one, when js code is present to alter table without refresh:
@login_required
def add_to_cart_next_view(request, slug):
    add_to_cart(request, slug)
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


@login_required
def remove_from_cart_view(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, complete=False)
    if order_qs.exists():
        order = order_qs[0]
        # Get the OrderItem(s) referencing this order and product
        order_items = OrderItem.objects.filter(order=order, product=item)
        if order_items.exists():
            order_items[0].delete()
            messages.info(request, item.name + ' removed from your cart')
            return redirect("store:order_summary")

    messages.info(request, 'Your cart does not contain any ' + item.name)
    return redirect("store:order_summary")

@login_required
def remove_single_item_from_cart_view(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, complete=False)
    if order_qs.exists():
        order = order_qs[0]
        # Get the OrderItem(s) referencing this order and product
        order_items = OrderItem.objects.filter(order=order, product=item)
        if order_items.exists():
            # order_items[0].quantity += request.quantity
            existing_order_item = order_items[0]
            existing_order_item.quantity -= 1
            existing_order_item.save()
            messages.info(request, 'Your cart has been updated')
    return redirect("store:order_summary")



class OrderSummaryView(View):
    def get(self, *args, **kwargs):

        try:
            order = Order.objects.get(user=self.request.user, complete=False)
            ctx = {'order': order }
            return render(self.request, "order_summary.html", ctx)
        except ObjectDoesNotExist:
            messages.error(self.request, "You haven't added any product in your basket yet")
            return redirect('/')

    

order_summary_view = login_required(OrderSummaryView.as_view())