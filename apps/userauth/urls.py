from django.urls import path, include
from .views import AddressView, CustomerView, ManagerView, SupplierView, UserView, customer_signup, supplier_signup, manager_signup
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'addresses', AddressView, 'address')
router.register(r'users', UserView, 'address')
router.register(r'customers', CustomerView, 'customer')
router.register(r'suppliers', SupplierView, 'supplier')
router.register(r'managers', ManagerView, 'manager')

urlpatterns = [
    path('signup/', customer_signup, name='customer_signup'),
    path('signup/supplier/', supplier_signup, name='supplier_signup'),
    path('signup/manager/', manager_signup, name='manager_signup'),
    path('api/userauth/', include(router.urls)),
]
