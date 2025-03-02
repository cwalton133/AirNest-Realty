from django.urls import path
from . import views
from .views import UserRegisterAPIView, UserLoginAPIView, PasswordResetListCreateAPIView


urlpatterns = [

    path(' ', views.Home, name='home'),
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('forgot-password/', views.ForgotPassword, name='forgot-password'),
    path('password-reset-sent/<str:reset_id>/',
         views.PasswordResetSent, name='password-reset-sent'),
    path('reset-password/<str:reset_id>/',
         views.ResetPassword, name='reset-password'),
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('password_reset/', PasswordResetListCreateAPIView.as_view(),
         name='password-reset-list-create'),
]
