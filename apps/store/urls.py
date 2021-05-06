from django.urls import path
from .views import product_list

app_name = "store"

urlpatterns = [
    path('products/', product_list, name="product_list"),
]
