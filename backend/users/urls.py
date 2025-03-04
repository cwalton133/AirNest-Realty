from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import RegisterAPIView, LoginAPIView, LogoutAPIView, GoogleLoginAPIView, UserProfileAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('profile/', UserProfileAPIView.as_view(), name="profile"),

    # JWT Authentication
    path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),

    # Google OAuth2 Login
    path('google-login/', GoogleLoginAPIView.as_view(), name="google-login"),
]
