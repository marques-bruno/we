from django.urls import path
from .views import product_list_view, product_detail_view, add_to_cart_view, add_to_cart_next_view

app_name = "store"

urlpatterns = [
    path('products/', product_list_view, name="product_list"),
    path('product/<slug>/', product_detail_view, name="product"),
    path('add-to-cart/<slug>/', add_to_cart_view, name="add_to_cart"),
    path('add-to-cart-next/<slug>/', add_to_cart_next_view, name="add_to_cart_next"),
]
