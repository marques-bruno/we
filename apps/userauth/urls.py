from django.urls import path
from .views import profile_view, supplier_profile_view, CustomUserUpdateView, CustomUserDeleteView, CustomerUserSignupView, SupplierUserSignupView, ManagerUserSignupView


urlpatterns = [
    path('profile/', profile_view, name="account_profile"),
    path('profile/supplier/', supplier_profile_view, name="supplier_account_profile"),
    path('<int:pk>/update/', CustomUserUpdateView.as_view(template_name='account/update.html'), name='account_update'),
    path('<int:pk>/delete/', CustomUserDeleteView.as_view(template_name='account/delete.html'), name='account_delete'),
    path('signup/', CustomerUserSignupView.as_view(template_name='account/signup.html'), name='customer_signup'),
    path('signup/supplier/', SupplierUserSignupView.as_view(template_name='account/supplier_signup.html'), name='supplier_signup'),
    path('signup/manager/', ManagerUserSignupView.as_view(template_name='account/manager_signup.html'), name='manager_signup'),
]
