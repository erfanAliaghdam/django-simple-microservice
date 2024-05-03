from unittest.mock import patch
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from model_bakery import baker
from core.tests.base import BaseTestClass
from user.repositories import UserRepository


class UserRepositoryTest(BaseTestClass):
    def setUp(self) -> None:
        super().setUp()
        self.user_repository = UserRepository()
        self.client_group = baker.make(Group, name="Client")

    @patch("user.repositories.user_repository.UserRepository.filter_user_by_email")
    def test_check_if_client_user_exists_existing_user_returns_true(
        self, user_query_mock
    ):
        user_query_mock.return_value = get_user_model().objects.filter(
            email=self.user.email
        )
        self.assertTrue(
            self.user_repository.check_if_client_user_exists(email=self.user.email)
        )

    @patch("user.repositories.user_repository.UserRepository.filter_user_by_email")
    def test_check_if_client_user_exists_non_existing_user_returns_false(
        self, user_query_mock
    ):
        email = "invalid@example.com"
        user_query_mock.return_value = get_user_model().objects.filter(email=email)
        self.assertFalse(self.user_repository.check_if_client_user_exists(email=email))

    @patch("user.repositories.user_repository.Group.objects.filter")
    @patch("user.models.user_model.UserManager.create_user")
    def test_register_client_user(self, user_create_mock, group_mock):
        group_mock.return_value.first.return_value = self.client_group
        user_create_mock.return_value = self.user
        user = self.user_repository.register_client_user(
            first_name="",
            last_name="",
            email="",
            password="",
        )
        self.assertEqual(user.id, self.user.id)
        self.assertEqual(user.groups.first().name, "Client")
