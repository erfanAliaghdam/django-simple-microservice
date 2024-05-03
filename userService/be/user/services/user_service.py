import logging
from django.db import transaction
from core.exceptions import Custom500Exception
from user.repositories import UserRepository
from app.producer import publish
from user.api.v1.serializers import UserMinSerializer
import json


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_client_user(
        self, first_name: str, last_name: str, email: str, password: str
    ):
        try:
            with transaction.atomic():
                user = self.user_repository.register_client_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                )
                user_data = UserMinSerializer(user).data
                publish("user_registered", json.dumps(user_data), "mail")
                return user
        except Exception as e:
            logging.error(f"Failed on register client user. {e}")
            raise Custom500Exception("something went wrong. please try again later.")
