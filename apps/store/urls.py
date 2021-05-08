from django.urls import path
from .views import (
    product_list_view,
    product_detail_view,
    add_to_cart_view,
    add_to_cart_next_view,
    remove_from_cart_view,
    order_summary_view,
    remove_single_item_from_cart_view,
    add_single_item_from_cart_view,
)

app_name = "store"

urlpatterns = [
    path('products/', product_list_view, name="product_list"),
    path('product/<slug>/', product_detail_view, name="product"),
    path('add-to-cart/<slug>/', add_to_cart_view, name="add_to_cart"),
    path('remove-from-cart/<slug>/', remove_from_cart_view, name="remove_from_cart"),
    path('add-single-item-from-cart/<slug>/', add_single_item_from_cart_view, name="add_single_item_from_cart"),
    path('remove-single-item-from-cart/<slug>/', remove_single_item_from_cart_view, name="remove_single_item_from_cart"),
    # @todo: remove later one, when js code is present to alter table without refresh:
    path('add-to-cart-next/<slug>/', add_to_cart_next_view, name="add_to_cart_next"),
    path('order-summary/', order_summary_view, name="order_summary"),
]
