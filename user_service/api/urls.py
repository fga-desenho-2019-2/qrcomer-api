from django.urls import path
from .views import CreateUserProfile, UserProfile, UserProfileView, MyTokenObtainPairView
from django.conf.urls import include

urlpatterns = [
  path('user/', CreateUserProfile.as_view(), name='post_user'),
  path('user/<int:id>', UserProfile.as_view(), name='get_user'),
  path('user/list/', UserProfileView.as_view(), name='list_user'),
  path('token/', MyTokenObtainPairView.as_view(), name='get_token' )
  # path('user', post_user, name='post_user'),
  # path('user/<str:cpf>', UserProfile.as_view(), name='get'),
  # path('user/<str:cpf>', delete_user, name='delete_user'),
]
