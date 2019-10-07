from django.urls import path
from user_service.api.views import (
  users,
  user,
)

urlpatterns = [
  path('user/<int:id>', user, name="user"),
  path('users', users, name='user'),
]
