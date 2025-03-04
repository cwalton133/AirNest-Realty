from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from social_django.utils import load_strategy
from social_core.backends.google import GoogleOAuth2
from social_core.exceptions import AuthException
from users.serializers import UserSerializer
import requests

User = get_user_model()

# Generate JWT Token


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class GoogleLoginAPIView(APIView):
    """ Handles login/signup with Google OAuth2 """

    def post(self, request):
        token = request.data.get("token")
        if not token:
            return Response({"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Verify the Google token
            google_oauth_url = f"https://oauth2.googleapis.com/tokeninfo?id_token={token}"
            response = requests.get(google_oauth_url)
            user_data = response.json()

            if "email" not in user_data:
                return Response({"error": "Invalid Google token"}, status=status.HTTP_400_BAD_REQUEST)

            email = user_data["email"]
            first_name = user_data.get("given_name", "")
            last_name = user_data.get("family_name", "")

            # Check if user already exists
            user, created = User.objects.get_or_create(email=email, defaults={
                "username": email.split("@")[0],
                "first_name": first_name,
                "last_name": last_name,
            })

            # Generate JWT tokens
            tokens = get_tokens_for_user(user)

            return Response({
                "message": "User logged in successfully",
                "tokens": tokens,
                "user": UserSerializer(user).data,
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RegisterAPIView(generics.CreateAPIView):
    """ Registers a new user """
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class LoginAPIView(APIView):
    """ Authenticates user and provides JWT tokens """

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = User.objects.filter(email=email).first()
        if user and user.check_password(password):
            tokens = get_tokens_for_user(user)
            return Response({"tokens": tokens, "user": UserSerializer(user).data}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    """ Logs out a user by blacklisting the refresh token """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logged out successfully"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(generics.RetrieveAPIView):
    """ Retrieves user profile details """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
