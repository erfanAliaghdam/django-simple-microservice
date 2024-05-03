from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


class UserRepository:
    def __init__(self):
        self.user_model = get_user_model()

    def filter_user_by_email(self, email: str):
        return self.user_model.objects.filter(email=email)

    def check_if_client_user_exists(self, email: str):
        if not self.filter_user_by_email(email).exists():
            return False
        return True

    def register_client_user(
        self, first_name: str, last_name: str, email: str, password: str
    ):
        user = self.user_model.objects.create_user(
            first_name=first_name, last_name=last_name, email=email, password=password
        )
        client_group, _ = Group.objects.get_or_create(name="Client")
        user.groups.add(client_group)
        user.refresh_from_db()
        return user
