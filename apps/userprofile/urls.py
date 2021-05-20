from django.urls import path
from .views import profile_view, account_dashboard_view, account_update_view, account_delete_view, account_message_board_view


urlpatterns = [
    path('profile/', profile_view, name="account_profile"),
    path('<int:pk>/profile/dashboard/', account_dashboard_view, name="account_dashboard"),
    path('<int:pk>/profile/update/', account_update_view, name='account_update'),
    path('<int:pk>/profile/message-board/', account_message_board_view, name='account_message_board'),
    path('<int:pk>/profile/delete/', account_delete_view, name='account_delete'),
]
