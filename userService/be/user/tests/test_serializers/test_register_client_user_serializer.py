from django.contrib.auth import get_user_model
from django.test import TestCase
from model_bakery import baker
from user.api.v1.serializers import RegisterClientUserSerializer


class RegisterClientUserSerializerTest(TestCase):
    def setUp(self) -> None:
        self.valid_data = {
            "first_name": "test first name",
            "last_name": "test last name",
            "email": "valid-test-user@example.com",
            "password": "Pass123@#$",
            "fcm_token": "test-token",
        }

    def test_validate_first_name_blank(self):
        self.invalid_data = self.valid_data.copy()
        self.invalid_data["first_name"] = ""
        serializer = RegisterClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("first_name", serializer.errors)
        self.assertEqual(
            str(serializer.errors["first_name"][0]), "first name is invalid."
        )

    def test_validate_first_name_null(self):
        self.invalid_data = self.valid_data.copy()
        self.invalid_data["first_name"] = None
        serializer = RegisterClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("first_name", serializer.errors)
        self.assertEqual(
            str(serializer.errors["first_name"][0]), "first name is invalid."
        )

    def test_validate_first_name_invalid(self):
        self.invalid_data = self.valid_data.copy()
        self.invalid_data["first_name"] = []
        serializer = RegisterClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("first_name", serializer.errors)
        self.assertEqual(
            str(serializer.errors["first_name"][0]), "first name is invalid."
        )

    def test_validate_first_name_required(self):
        self.invalid_data = self.valid_data.copy()
        del self.invalid_data["first_name"]
        serializer = RegisterClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("first_name", serializer.errors)
        self.assertEqual(
            str(serializer.errors["first_name"][0]), "first name is required."
        )

    def test_validate_last_name_blank(self):
        self.invalid_data = self.valid_data.copy()
        self.invalid_data["last_name"] = ""
        serializer = RegisterClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("last_name", serializer.errors)
        self.assertEqual(
            str(serializer.errors["last_name"][0]), "last name is invalid."
        )

    def test_validate_last_name_null(self):
        self.invalid_data = self.valid_data.copy()
        self.invalid_data["last_name"] = None
        serializer = RegisterClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("last_name", serializer.errors)
        self.assertEqual(
            str(serializer.errors["last_name"][0]), "last name is invalid."
        )

    def test_validate_last_name_invalid(self):
        self.invalid_data = self.valid_data.copy()
        self.invalid_data["last_name"] = []
        serializer = RegisterClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("last_name", serializer.errors)
        self.assertEqual(
            str(serializer.errors["last_name"][0]), "last name is invalid."
        )

    def test_validate_last_name_required(self):
        self.invalid_data = self.valid_data.copy()
        del self.invalid_data["last_name"]
        serializer = RegisterClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("last_name", serializer.errors)
        self.assertEqual(
            str(serializer.errors["last_name"][0]), "last name is required."
        )

    def test_validate_email_blank(self):
        self.invalid_data = self.valid_data.copy()
        self.invalid_data["email"] = ""
        serializer = RegisterClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)
        self.assertEqual(str(serializer.errors["email"][0]), "email is invalid.")

    def test_validate_email_null(self):
        self.invalid_data = self.valid_data.copy()
        self.invalid_data["email"] = None
        serializer = RegisterClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)
        self.assertEqual(str(serializer.errors["email"][0]), "email is invalid.")

    def test_validate_email_invalid(self):
        self.invalid_data = self.valid_data.copy()
        self.invalid_data["email"] = []
        serializer = RegisterClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)
        self.assertEqual(str(serializer.errors["email"][0]), "email is invalid.")

    def test_validate_email_required(self):
        self.invalid_data = self.valid_data.copy()
        del self.invalid_data["email"]
        serializer = RegisterClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)
        self.assertEqual(str(serializer.errors["email"][0]), "email is required.")

    def test_validate_password_blank(self):
        self.invalid_data = self.valid_data.copy()
        self.invalid_data["password"] = ""
        serializer = RegisterClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)
        self.assertEqual(str(serializer.errors["password"][0]), "password is invalid.")

    def test_validate_password_null(self):
        self.invalid_data = self.valid_data.copy()
        self.invalid_data["password"] = None
        serializer = RegisterClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)
        self.assertEqual(str(serializer.errors["password"][0]), "password is invalid.")

    def test_validate_password_invalid(self):
        self.invalid_data = self.valid_data.copy()
        self.invalid_data["password"] = []
        serializer = RegisterClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)
        self.assertEqual(str(serializer.errors["password"][0]), "password is invalid.")

    def test_validate_password_required(self):
        self.invalid_data = self.valid_data.copy()
        del self.invalid_data["password"]
        serializer = RegisterClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)
        self.assertEqual(str(serializer.errors["password"][0]), "password is required.")

    def test_validate_insecure_password(self):
        self.invalid_data = self.valid_data.copy()
        self.invalid_data["password"] = "short"
        serializer = RegisterClientUserSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)
        self.assertEqual(
            str(serializer.errors["password"][0]),
            "This password is too short. It must contain at least 8 characters.",
        )

    def test_serializer_validate_existing_email(self):
        existing_user = baker.make(get_user_model())
        self.valid_data["email"] = existing_user.email
        serializer = RegisterClientUserSerializer(data=self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)
        self.assertEqual(
            str(serializer.errors["email"][0]), "User with this email exists."
        )
