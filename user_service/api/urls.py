from django.urls import path
from .views import (
        CreateUserProfile, UserProfile, UserProfileView, 
        ProfileCards, MyTokenObtainPairView,
        EditUserProfile, CreateCard, CardView,
        CreateUserImage, GetUserImage, DeleteUserImage
    )
from django.conf.urls import include

urlpatterns = [
    path('user/', CreateUserProfile.as_view(), name='post_user'),
    path('get_user/<str:cpf>', UserProfile.as_view(), name='get_user'),
    path('edit_user/<str:cpf>', EditUserProfile.as_view(), name='edit_user'),
    path('user/list/', UserProfileView.as_view(), name='list_user'),
    path('token/', MyTokenObtainPairView.as_view(), name='get_token'),
    # path('user/<str:cpf>', delete_user, name='delete_user'),

    ## user cards urls

    path('user/card/', CreateCard.as_view(), name='post_card'),
    path('user/card/<int:id>', CardView.as_view(), name='get_card'),
    # path('user/card/<int:id>', CardView.as_view(), name='put_card'),
    path('user/user_cards/', ProfileCards.as_view(), name='get_profile_card'),
    
    ## user images urls
    path('user/post_image', CreateUserImage.as_view(), name='post_image'),
    path('user/get_image/<str:cpf>', GetUserImage.as_view(), name='get_image'),
    path('user/delete_image/<str:cpf>', DeleteUserImage.as_view(), name='delete_image')
]
