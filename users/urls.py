from django.urls import path
from .views import RegisterUserView, UserView, AllUsersView, ResetPassword, APILogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', AllUsersView.as_view()),
    path('user/', UserView.as_view()),
    path('register/', RegisterUserView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("password-reset/", ResetPassword.as_view(), name="password_reset"),
    path("logout/", APILogoutView.as_view(), name="logout"),
]