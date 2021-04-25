from django.urls import path
from .views import profile_view, supplier_profile_view, user_update_view, user_delete_view


urlpatterns = [
    path('profile/', profile_view, name="account_profile"),
    path('profile/supplier/', supplier_profile_view, name="supplier_account_profile"),
    path('<int:pk>/update/', user_update_view, name='account_update'),
    path('<int:pk>/delete/', user_delete_view, name='account_delete'),
]
