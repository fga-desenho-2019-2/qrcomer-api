from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('api/', include('user_service.api.urls')),
    path('admin/', admin.site.urls),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include('rest_framework.urls')),

]
