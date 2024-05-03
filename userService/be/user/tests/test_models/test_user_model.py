from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.test import TestCase


class UserModelTest(TestCase):
    def test_user_model_is_inherited_from_abstract_user(self):
        self.assertTrue(issubclass(get_user_model(), AbstractUser))

    def test_user_model_has_correct_attributes(self):
        user_obj = get_user_model()
        self.assertTrue(hasattr(user_obj, "id"))
        self.assertTrue(hasattr(user_obj, "password"))
        self.assertTrue(hasattr(user_obj, "last_login"))
        self.assertTrue(hasattr(user_obj, "is_superuser"))
        self.assertTrue(hasattr(user_obj, "first_name"))
        self.assertTrue(hasattr(user_obj, "last_name"))
        self.assertTrue(hasattr(user_obj, "email"))
        self.assertTrue(hasattr(user_obj, "is_staff"))
        self.assertTrue(hasattr(user_obj, "is_active"))
        self.assertTrue(hasattr(user_obj, "date_joined"))
        self.assertTrue(hasattr(user_obj, "updated_at"))
        self.assertTrue(hasattr(user_obj, "fcm_token"))

    def test_create_user_with_email_successfully(self):
        email = "test@example.com"
        password = "Test123456"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_is_normalized(self):
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "Test!@$@$1234")
            self.assertEqual(user.email, expected)
            user.delete()

    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "test12adsad3")

    def test_create_superuser_successfully(self):
        superuser = get_user_model().objects.create_superuser(
            "test_superuser@example.com", "test1231123413"
        )

        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

    def test_auto_populated_unique_username(self):
        email = "test@example.com"
        password = "Test123456"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertIsNotNone(user.user_identifier)
        self.assertEqual(len(user.user_identifier), 17)
