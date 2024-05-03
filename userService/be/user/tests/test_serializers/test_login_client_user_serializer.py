from django.test import TestCase
from user.api.v1.serializers import LoginClientUserSerializer


class LoginClientUserSerializerTest(TestCase):
    def setUp(self) -> None:
        self.valid_data = {
            "first_name": "test first name",
            "last_name": "test last name",
            "email": "valid-test-user@example.com",
            "password": "Pass123@#$",
            "fcm_token": "test-token",
        }

    def test_validate_email_blank(self):
        self.invalid_data = self.valid_data.copy()
        self.invalid_data["email"] = ""
        serializer = LoginClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)
        self.assertEqual(str(serializer.errors["email"][0]), "email is invalid.")

    def test_validate_email_null(self):
        self.invalid_data = self.valid_data.copy()
        self.invalid_data["email"] = None
        serializer = LoginClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)
        self.assertEqual(str(serializer.errors["email"][0]), "email is invalid.")

    def test_validate_email_invalid(self):
        self.invalid_data = self.valid_data.copy()
        self.invalid_data["email"] = []
        serializer = LoginClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)
        self.assertEqual(str(serializer.errors["email"][0]), "email is invalid.")

    def test_validate_email_required(self):
        self.invalid_data = self.valid_data.copy()
        del self.invalid_data["email"]
        serializer = LoginClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)
        self.assertEqual(str(serializer.errors["email"][0]), "email is required.")

    def test_validate_password_blank(self):
        self.invalid_data = self.valid_data.copy()
        self.invalid_data["password"] = ""
        serializer = LoginClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)
        self.assertEqual(str(serializer.errors["password"][0]), "password is invalid.")

    def test_validate_password_null(self):
        self.invalid_data = self.valid_data.copy()
        self.invalid_data["password"] = None
        serializer = LoginClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)
        self.assertEqual(str(serializer.errors["password"][0]), "password is invalid.")

    def test_validate_password_invalid(self):
        self.invalid_data = self.valid_data.copy()
        self.invalid_data["password"] = []
        serializer = LoginClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)
        self.assertEqual(str(serializer.errors["password"][0]), "password is invalid.")

    def test_validate_password_required(self):
        self.invalid_data = self.valid_data.copy()
        del self.invalid_data["password"]
        serializer = LoginClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)
        self.assertEqual(str(serializer.errors["password"][0]), "password is required.")
