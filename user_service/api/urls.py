from django.urls import path
from .views import CreateUserProfile, UserProfile, UserProfileView, UserCardCreate, UserCardGetData#, UserCardsUpdate
from django.conf.urls import include

urlpatterns = [
  path('user/', CreateUserProfile.as_view(), name='post-user'),
  path('user/<int:id>', UserProfile.as_view(), name='get-user'),
  path('user/list/', UserProfileView.as_view(), name='list-users'),
  # path('user/<str:cpf>', UserProfile.as_view(), name='get'),
  # path('user/<str:cpf>', delete_user, name='delete_user'),

  ## user cards urls

  path('user/card/', UserCardCreate.as_view(), name='post-user-card'),
  path('user/card/<int:id>', UserCardGetData.as_view(), name='get-user-card'),
  # path('user/card/<int:id>', UserCardsUpdate.as_view(), name='patch-user-card')
]
