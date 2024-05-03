from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.conf import settings
import random


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address. ")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(max_length=255, unique=True)
    user_identifier = models.CharField(
        max_length=255, unique=True, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    fcm_token = models.CharField(max_length=255, null=True, blank=True)
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users (All)"

    def save(self, *args, **kwargs) -> None:
        if not self.user_identifier:
            unique_id = self.unique_id_maker()
            unique = False
            while not unique:
                if (
                    not get_user_model()
                    .objects.filter(user_identifier=unique_id)
                    .exists()
                ):
                    unique = True
                else:
                    unique_id = None
                    unique_id = self.unique_id_maker()
            self.user_identifier = unique_id
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.email)

    @staticmethod
    def unique_id_maker():
        return f"{settings.USER_IDENTIFIER_PREFIX}_" + str(
            random.randint(000000000000, 999999999999)
        ).zfill(12)
