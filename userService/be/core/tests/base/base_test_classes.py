from django.contrib.auth.models import Group
from django.test import TestCase
from django.contrib.auth import get_user_model, authenticate
from model_bakery import baker
from rest_framework.test import APIClient


class BaseTestClass(TestCase):
    def setUp(self) -> None:
        self.user_password = "DefaultPassword"
        self.user = baker.make(get_user_model())
        self.user.set_password(self.user_password)
        self.user.save()


class BaseAPITestClass(BaseTestClass):
    def setUp(self) -> None:
        super().setUp()
        self.client = APIClient()

    def authenticate_user(self, user):
        self.client.force_authenticate(user)

