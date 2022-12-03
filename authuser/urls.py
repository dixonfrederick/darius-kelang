from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from .views import getBalance
urlpatterns = [
    path('test/', getBalance),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
