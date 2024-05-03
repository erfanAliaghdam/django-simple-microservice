from rest_framework.exceptions import APIException
from rest_framework import status


class Custom403Exception(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "You are not allowed to do this action."
