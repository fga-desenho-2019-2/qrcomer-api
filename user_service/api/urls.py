from django.urls import path
from user_service.api.views import (
  users,
  user,
)

urlpatterns = [
    # path('register_client/', register_client, name='register_client'),
    path('user/', user, name="user"),
    path('users/', users, name='user'),
    # path('edit_client/<int:registro>', edit_client, name='edit_client'),
    # path('delete_client/<int:registro>', delete_client, name='delete_client')

]
