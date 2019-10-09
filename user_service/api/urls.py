from django.urls import path
from user_service.api.views import (
  users,
  get_user,
  post_user,
  patch_user,
  delete_user
)
from django.conf.urls import url, include

urlpatterns = [
  path('users', users, name='users'),
  path('user/<str:cpf>', get_user, name="get_user"),
  path('user', post_user, name='post_user'),
  path('user/<str:cpf>', patch_user, name='patch_user'),
  path('user/<str:cpf>', delete_user, name='delete_user'),
]
