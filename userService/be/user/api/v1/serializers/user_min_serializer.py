from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email", "first_name", "last_name"]
