from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.contrib import messages
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

def add_to_cart_view(request, slug):
    add_to_cart(request, slug)
    return redirect("store:product", slug=slug)

def add_to_cart_next_view(request, slug):
    add_to_cart(request, slug)
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)