from django.urls import path
from .views import profile_view, CustomUserUpdateView, CustomUserDeleteView, SupplierUserRegistrationView, ManagerUserRegistrationView


urlpatterns = [
    path('profile/', profile_view, name="account_profile"),
    path('<int:pk>/update/', CustomUserUpdateView.as_view(template_name='account/update.html'), name='account_update'),
    path('<int:pk>/delete/', CustomUserDeleteView.as_view(template_name='account/delete.html'), name='account_delete'),
    path('signup-supplier/', SupplierUserRegistrationView.as_view(template_name='account/signup-supplier.html'), name='signup-supplier'),
    path('signup-manager/', ManagerUserRegistrationView.as_view(template_name='account/signup-manager.html'), name='signup-manager'),
]
