from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class CustomEmailBackend(BaseBackend):
    """Custom authentication backend. Allows users to log in using their email address."""

    def authenticate(self, request, email=None, password=None, **kwargs):
        """Overrides the authenticate method to allow users to log in using their email address."""
        User = get_user_model()

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """Overrides the get_user method to allow users to log in using their email address."""
        User = get_user_model()

        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None