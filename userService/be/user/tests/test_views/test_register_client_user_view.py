from unittest.mock import patch
from django.urls import reverse
from rest_framework.authtoken.models import Token
from core.tests.base import BaseAPITestClass


class RegisterClientUserViewTest(BaseAPITestClass):
    def setUp(self) -> None:
        super().setUp()
        self.url = reverse("register-client")
        self.valid_data = {
            "first_name": "test first name",
            "last_name": "test last name",
            "email": "valid-test-user@example.com",
            "password": "Pass123@#$",
        }
        self.invalid_data = {"invalid": "invalid"}

    @patch("user.api.v1.views.register_client_user_views.UserService.register_client_user")
    @patch("user.api.v1.views.register_client_user_views.Token.objects.get_or_create")
    def test_user_can_register_successfully_returns_201(
        self, token_mock, register_client_service_mock
    ):
        token = "mocked_token_key"
        token_mock.return_value = (Token(key=token), False)
        register_client_service_mock.return_value = self.user
        response = self.client.post(self.url, data=self.valid_data)
        register_client_service_mock.assert_called_once_with(
            first_name=self.valid_data["first_name"],
            last_name=self.valid_data["last_name"],
            email=self.valid_data["email"],
            password=self.valid_data["password"],
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], "success")
        self.assertEqual(response.data["message"], "Client registered successfully.")
        self.assertEqual(response.data["data"]["token"], token)

    def test_invalid_serializer_returns_400_response(self):
        response = self.client.post(self.url, data=self.invalid_data)
        self.assertEqual(response.status_code, 400)

    def token_creation_failure(*args, **kwargs):
        raise Exception("Simulated token creation failure")

    @patch("user.api.v1.views.register_client_user_views.logging.error")
    @patch(
        "user.api.v1.views.register_client_user_views.UserService.register_client_user"
    )
    @patch("user.api.v1.views.register_client_user_views.Token.objects.get_or_create")
    def test_500_error_handling(
        self, token_mock, register_client_service_mock, logging_mock
    ):
        token = "mocked_token_key"
        token_mock.return_value = (Token(key=token), False)
        token_mock.side_effect = lambda *args, **kwargs: Exception(
            "Simulated token creation failure"
        )
        register_client_service_mock.return_value = self.user
        response = self.client.post(self.url, data=self.valid_data)
        register_client_service_mock.assert_called_once_with(
            first_name=self.valid_data["first_name"],
            last_name=self.valid_data["last_name"],
            email=self.valid_data["email"],
            password=self.valid_data["password"],
        )
        self.assertEqual(response.status_code, 500)
        logging_mock.assert_called_once()
