from rest_framework import serializers


class LoginClientUserSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        max_length=255,
        error_messages={
            "invalid": "email is invalid.",
            "required": "email is required.",
            "blank": "email is invalid.",
            "null": "email is invalid.",
        },
    )
    password = serializers.CharField(
        required=True,
        max_length=255,
        error_messages={
            "invalid": "password is invalid.",
            "required": "password is required.",
            "blank": "password is invalid.",
            "null": "password is invalid.",
        },
    )
