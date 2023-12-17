from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserRegister, UserListAPIView, UserDestroyAPIView, UserAuthorizationView, PasswordRecoveryView, \
    RequestPasswordRecoveryView, UserUpdateAPIView

app_name = UsersConfig.name

router = routers.DefaultRouter()

urlpatterns = [
    path('', UserListAPIView.as_view(), name='users'),
    path('sign-up/', UserRegister.as_view(), name='user_register'),
    path('sign-in/', UserAuthorizationView.as_view(), name='user_authorization'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserDestroyAPIView.as_view(), name='user_delete'),

    path('recovery/', RequestPasswordRecoveryView.as_view(), name='password_recovery'),
    path('recovery/<str:hash>/', PasswordRecoveryView.as_view(), name='password_recovery'),

    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
