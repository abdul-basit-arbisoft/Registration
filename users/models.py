from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom User Model Class"""

    MALE = "M"
    FEMALE = "F"
    OTHER = "O"
    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
    ]

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_super_user = models.BooleanField(default=False)
    date_joined =models.DateTimeField(default=timezone.now)
    birth_date = models.DateField(blank=True, null=True, default=None)
    address = models.TextField(blank=True, null=True)
    contact_no = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    age = models.IntegerField(default=18)
    profile_pic = models.ImageField(upload_to='Images', blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        """Meta data class"""

        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        """string representation of the instance."""
        return self.email