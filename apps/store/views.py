from .forms import ProductForm
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.views.generic import View, DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from rest_framework import serializers
# from rest_framework.serializers import Serializer
from .store_models import (
    Order,
    OrderItem,
    OrderStatus,
    ProductAllergen,
    PickupPoint,
    ProductUnit,
    ProductType,
    ProductLabel,
    Product,
)

#######################REST_API#########################

from rest_framework import serializers, viewsets
from .serializers import (
    OrderSerializer,
    OrderItemSerializer,
    OrderStatusSerializer,
    ProductSerializer,
    ProductAllergenSerializer,
    ProductLabelSerializer,
    ProductTypeSerializer,
    ProductUnitSerializer,
    PickupPointSerializer
)


class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderItemView(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()


class OrderStatusView(viewsets.ModelViewSet):
    serializer_class = OrderStatusSerializer
    queryset = OrderStatus.objects.all()


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductAllergenView(viewsets.ModelViewSet):
    serializer_class = ProductAllergenSerializer
    queryset = ProductAllergen.objects.all()


class ProductLabelView(viewsets.ModelViewSet):
    serializer_class = ProductLabelSerializer
    queryset = ProductLabel.objects.all()


class ProductTypeView(viewsets.ModelViewSet):
    serializer_class = ProductTypeSerializer
    queryset = ProductType.objects.all()


class ProductUnitView(viewsets.ModelViewSet):
    serializer_class = ProductUnitSerializer
    queryset = ProductUnit.objects.all()


class PickupPointView(viewsets.ModelViewSet):
    serializer_class = PickupPointSerializer
    queryset = PickupPoint.objects.all()

########################################################


def product_list_view(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, "product_list.html", context)


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"


product_detail_view = ProductDetailView.as_view()


@login_required
def ajax_add_to_cart(request):
    slug = request.GET.get('slug', None)
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, complete=False)
    n_items = 1
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
            n_items = OrderItem.objects.filter(order=order).count()
        else:
            # order_item = OrderItem.objects.create(product=item, order=order, quantity=request.quantity)
            order_item = OrderItem.objects.create(
                product=item, order=order, quantity=1)
            order_item.save()
            messages.info(request, item.name + 'x' +
                          str(order_item.quantity) + ' has been added to your cart')
            n_items = OrderItem.objects.filter(order=order).count()
    else:
        order = Order.objects.create(user=request.user)
        order.save()
        # order_item = OrderItem.objects.create(product=item, order=order, quantity=request.quantity)
        order_item = OrderItem.objects.create(
            product=item, order=order, quantity=1)
        order_item.save()
        messages.info(request, item.name + 'x' +
                      str(order_item.quantity) + ' has been added to your cart')
    django_messages = []
    for message in messages.get_messages(request):
        django_messages.append({
            "level": message.level,
            "message": message.message,
            "extra_tags": message.tags,
        })
    return JsonResponse({'n_items': n_items, 'messages': django_messages}, status=200)


@login_required
def ajax_increase_item_from_cart(request):
    slug = request.GET.get('slug', None)
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, complete=False)
    if order_qs.exists():
        order = order_qs[0]
        # Get the OrderItem(s) referencing this order and product
        order_items = OrderItem.objects.filter(order=order, product=item)
        if order_items.exists():
            existing_order_item = order_items[0]
            existing_order_item.quantity += 1
            existing_order_item.save()
            messages.info(request, 'Your cart has been updated')
            django_messages = []
            for message in messages.get_messages(request):
                django_messages.append({
                    "level": message.level,
                    "message": message.message,
                    "extra_tags": message.tags,
                })
            return JsonResponse({'n_items': order_items.count(), 'new_qtty': existing_order_item.quantity, 'messages': django_messages}, status=200)
    return JsonResponse({'error': 'An error occurred. please refresh the page'}, status=400)


@login_required
def ajax_decrease_item_from_cart(request):
    slug = request.GET.get('slug', None)
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
            django_messages = []
            for message in messages.get_messages(request):
                django_messages.append({
                    "level": message.level,
                    "message": message.message,
                    "extra_tags": message.tags,
                })
            return JsonResponse({'n_items': order_items.count(), 'new_qtty': existing_order_item.quantity, 'messages': django_messages}, status=200)
    return JsonResponse({'error': 'An error occurred. please refresh the page'}, status=400)


@login_required
def ajax_remove_item_from_cart(request):
    slug = request.GET.get('slug', None)
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, complete=False)
    django_messages = []
    if order_qs.exists():
        order = order_qs[0]
        # Get the OrderItem(s) referencing this order and product
        order_items = OrderItem.objects.filter(order=order, product=item)
        if order_items.exists():
            order_items[0].delete()
            messages.info(request, item.name + ' removed from your cart')
            for message in messages.get_messages(request):
                django_messages.append({
                    "level": message.level,
                    "message": message.message,
                    "extra_tags": message.tags,
                })
            return JsonResponse({'n_items': order_items.count(), 'removed': True, 'messages': django_messages}, status=200)
    messages.info(request, 'Your cart does not contain any ' + item.name)
    for message in messages.get_messages(request):
        django_messages.append({
            "level": message.level,
            "message": message.message,
            "extra_tags": message.tags,
        })
    return JsonResponse({'error': 'An error occurred. please refresh the page', 'messages': django_messages}, status=400)


class OrderSummaryView(View):
    def get(self, *args, **kwargs):

        try:
            order = Order.objects.get(user=self.request.user, complete=False)
            ctx = {'order': order}
            return render(self.request, "order_summary.html", ctx)
        except ObjectDoesNotExist:
            messages.error(
                self.request, "You haven't added any product in your basket yet")
            return redirect('/')


order_summary_view = login_required(OrderSummaryView.as_view())


@login_required
def ajax_get_product_info(request):
    slug = request.GET.get('slug', None)
    item = get_object_or_404(Product, slug=slug)
    #form = ProductForm()

    item_serializer = ProductSerializer(item)
    allergens = ProductAllergenSerializer(
        ProductAllergen.objects.all(), many=True)
    labels = ProductLabelSerializer(ProductLabel.objects.all(), many=True)
    types = ProductTypeSerializer(ProductType.objects.all(), many=True)

    data = {'item': item_serializer.data, 'all_allergens': allergens.data,
            'all_labels': labels.data, 'all_types': types.data}
    return JsonResponse(data, status=200)


@login_required
def ajax_set_product_info(request):
   # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        print("Do we even get to this point?" + str(request.POST))
        form = ProductForm(request.POST)
        # save the data and after fetch the object in instance

        ## Here it should be necessary to add product supplier (request.user)

        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)

