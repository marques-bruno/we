from django.urls import path
from .views import customer_signup, supplier_signup, manager_signup


urlpatterns = [
    path('signup/', customer_signup, name='customer_signup'),
    path('signup/supplier/', supplier_signup, name='supplier_signup'),
    path('signup/manager/', manager_signup, name='manager_signup'),
]
