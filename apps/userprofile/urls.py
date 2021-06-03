from django.urls import path
from .views import (
    account_calendar_view,
    account_documents_view,
    account_products_view,
    account_sales_view,
    profile_view,
    account_dashboard_view,
    account_update_view,
    account_delete_view,
    account_message_board_view
)

urlpatterns = [
    path('profile/', profile_view, name="account_profile"),
    path('<int:pk>/profile/dashboard/', account_dashboard_view, name="account_dashboard"),
    path('<int:pk>/profile/update/', account_update_view, name='account_update'),
    path('<int:pk>/profile/message-board/', account_message_board_view, name='account_message_board'),
    path('<int:pk>/profile/delete/', account_delete_view, name='account_delete'),
    path('<int:pk>/profile/my-sales/', account_sales_view, name='my_sales'),
    path('<int:pk>/profile/my-products/', account_products_view, name='my_products'),
    path('<int:pk>/profile/my-calendar/', account_calendar_view, name='my_calendar'),
    path('<int:pk>/profile/my-documents/', account_documents_view, name='my_documents'),
]
