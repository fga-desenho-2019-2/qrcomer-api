from django.urls import path
from .views import CreateUserProfile, UserProfileView, UserProfile
from django.conf.urls import url, include

urlpatterns = [
  path('user/', CreateUserProfile.as_view(), name='post_user'),
  path('user/<str:cpf>', UserProfile.as_view(), name='get_user'),
  path('user/list/', UserProfileView.as_view(), name='list_user'),
  # path('user', post_user, name='post_user'),
  # path('user/<str:cpf>', UserProfile.as_view(), name='get'),
  # path('user/<str:cpf>', delete_user, name='delete_user'),
]
