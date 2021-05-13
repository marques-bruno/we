from django.urls import path, include
from .views import AddressView, customer_signup, supplier_signup, manager_signup
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'addresses', AddressView, 'address')

urlpatterns = [
    path('signup/', customer_signup, name='customer_signup'),
    path('signup/supplier/', supplier_signup, name='supplier_signup'),
    path('signup/manager/', manager_signup, name='manager_signup'),
    path('api/userauth/', include(router.urls)),
]
