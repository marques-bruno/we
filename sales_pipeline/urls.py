from django.urls import path
from .views import (
    billing_view
)

app_name = "sales_pipeline"

urlpatterns = [
    path('billing/', billing_view, name="billing"),
]
