
from unittest.mock import patch
from django.contrib.auth import get_user_model
from django.test import TestCase
from model_bakery import baker
from core.exceptions import Custom500Exception
from user.services import UserService


class UserServiceTest(TestCase):
    def setUp(self) -> None:
        self.service = UserService()
        self.valid_data = {
            "first_name": "test first name",
            "last_name": "test last name",
            "email": "valid-test-user@example.com",
            "password": "Pass123@#$",
        }
        self.user = baker.make(get_user_model())

    @patch("user.services.user_service.UserMinSerializer.data")
    @patch("user.services.user_service.UserRepository.register_client_user")
    @patch("user.services.user_service.publish")
    @patch("user.services.user_service.json.dumps")
    def test_register_client_user_successfully(
        self,
        json_mock,
        publish_mock, 
        user_repository_mock,
        serializer_mock  
    ):
        user_repository_mock.return_value = self.user
        json_mock.return_value = None
        serializer_mock.return_value = None
        self.service.register_client_user(
            first_name=self.valid_data["first_name"],
            last_name=self.valid_data["last_name"],
            email=self.valid_data["email"],
            password=self.valid_data["password"],
        )
        user_repository_mock.assert_called_once_with(
            first_name=self.valid_data["first_name"],
            last_name=self.valid_data["last_name"],
            email=self.valid_data["email"],
            password=self.valid_data["password"],
        )
        publish_mock.asser_called_once_with("user_registered", None, "mail")

    @patch("user.services.user_service.logging")
    @patch("user.services.user_service.UserRepository.register_client_user")
    @patch("user.services.user_service.publish")
    def test_register_client_user_raise_500_exception(
        self, publish_mock, user_repository_mock, logging_mock
    ):
        user_repository_mock.side_effect = Exception("Simulated exception")

        with self.assertRaises(Custom500Exception):
            self.service.register_client_user(
                first_name=self.valid_data["first_name"],
                last_name=self.valid_data["last_name"],
                email=self.valid_data["email"],
                password=self.valid_data["password"],
            )
            user_repository_mock.assert_called_once_with(
                first_name=self.valid_data["first_name"],
                last_name=self.valid_data["last_name"],
                email=self.valid_data["email"],
                password=self.valid_data["password"],
            )
            logging_mock.assert_called_once()
