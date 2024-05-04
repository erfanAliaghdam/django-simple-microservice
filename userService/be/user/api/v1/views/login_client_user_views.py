from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from app.producer import publish
from datetime import datetime
from user.api.v1.serializers import LoginClientUserSerializer
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
import json


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def login_user_view(request):
    """
    input data:
        {
            "email": "johndoe@example.com",
            "password": "DefaultPassword"
        }
    """
    serializer = LoginClientUserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {
                "status": "failed",
                "message": "Invalid input.",
                "data": {"errors": serializer.errors},
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    # check if can authenticate user
    user = authenticate(email=request.data["email"], password=request.data["password"])
    if not user:
        return Response(
            {
                "status": "failed",
                "message": "Invalid input.",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    # get or create token
    token, _ = Token.objects.get_or_create(user=user)
    user_device = request.META.get("HTTP_USER_AGENT", None)
    user_ip = request.META.get("REMOTE_ADDR", None)
    user_id = user.id
    request_time = datetime.now()
    request_data = {
        "user_device": user_device,
        "user_ip": user_ip,
        "user_id": user_id,
        "request_time": int(request_time.timestamp()),
        "user_email": user.email
    }
    publish("user_logged_in", request_data, "log")
    return Response(
        {
            "status": "success",
            "message": "User token retrieved in successfully.",
            "data": {"token": token.key},
        },
        status=status.HTTP_200_OK,
    )
