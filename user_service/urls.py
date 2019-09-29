from django.urls import path
from django.conf.urls import url
from user_service import views
from .views import register_client, list_clients


urlpatterns = [
    path('register_client/', register_client, name='register_client'),
    path('list_clients/', list_clients, name='list_clients'),
    #path('edit_client/', edit_client, name='edit_client'),
    #path('get_client/', get_client, name='get_client')

]
