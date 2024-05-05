from unittest.mock import patch
from django.urls import reverse
from rest_framework.authtoken.models import Token
from core.tests.base import BaseAPITestClass


class LoginClientUserViewTest(BaseAPITestClass):
    def setUp(self) -> None:
        super().setUp()
        self.url = reverse("login-user")
        self.valid_data = {"email": self.user.email, "password": self.user_password}
        self.invalid_data = {"invalid": "invalid"}

    @patch("user.api.v1.views.login_client_user_views.get_client_ip")
    @patch("user.api.v1.views.login_client_user_views.publish")
    @patch("user.api.v1.views.login_client_user_views.authenticate")
    @patch("user.api.v1.views.login_client_user_views.Token.objects.get_or_create")
    def test_if_can_login_with_valid_data_returns_200(
        self, token_mock, authenticate_mock, publish_mock, get_ip_mock
    ):
        get_ip_mock.return_value = "ip"
        token = "mocked_token_key"
        token_mock.return_value = (Token(key=token), False)
        authenticate_mock.return_value = self.user
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], "success")
        self.assertEqual(
            response.data["message"], "User token retrieved in successfully."
        )
        publish_mock.assert_called_once()


    @patch("user.api.v1.views.login_client_user_views.authenticate")
    @patch("user.api.v1.views.login_client_user_views.Token.objects.get_or_create")
    def test_if_cannot_login_with_invalid_data_returns_400(
        self, token_mock, authenticate_mock
    ):
        token = "mocked_token_key"
        token_mock.return_value = (Token(key=token), False)
        authenticate_mock.return_value = self.user
        response = self.client.post(self.url, data=self.invalid_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["status"], "failed")
        self.assertEqual(response.data["message"], "Invalid input.")


    def test_if_cannot_login_with_invalid_credentials_data_returns_400(self):
        invalid_data = self.valid_data
        invalid_data["password"] = "invalid"
        response = self.client.post(self.url, data=invalid_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["status"], "failed")
        self.assertEqual(response.data["message"], "Invalid input.")
