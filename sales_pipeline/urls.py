from django.urls import path
from .views import (
    address_view,
    address_update_view,
    billing_view,
)

app_name = "sales_pipeline"

urlpatterns = [
    path('address/', address_view, name="address"),
    path('address/<int:pk>', address_update_view, name="update_address"),
    path('billing/', billing_view, name="billing"),
]
