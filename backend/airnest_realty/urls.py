from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from users.views import RegisterAPIView, LoginAPIView, LogoutAPIView, GoogleLoginAPIView, UserProfileAPIView


admin.site.site_header = 'AirNest Realty Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    # User Authentication API
    path('api/auth/register/', RegisterAPIView.as_view(), name="register"),
    path('api/auth/login/', LoginAPIView.as_view(), name="login"),
    path('api/auth/logout/', LogoutAPIView.as_view(), name="logout"),
    path('api/auth/profile/', UserProfileAPIView.as_view(), name="profile"),

    # JWT Token Authentication
    path('api/auth/token/', TokenObtainPairView.as_view(),
         name="token_obtain_pair"),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(),
         name="token_refresh"),

    # Google OAuth2 Authentication
    path('api/auth/google/', GoogleLoginAPIView.as_view(), name="google-login"),

]
