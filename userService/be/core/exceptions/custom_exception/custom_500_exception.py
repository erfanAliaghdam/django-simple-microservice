from rest_framework.exceptions import APIException
from rest_framework import status


class Custom500Exception(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "Internal server error, please try again later."
