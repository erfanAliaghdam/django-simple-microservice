from rest_framework.exceptions import APIException
from rest_framework import status


class Custom412Exception(APIException):
    status_code = status.HTTP_412_PRECONDITION_FAILED
    default_detail = "Pre-condition failed"
    errors = None

    def __init__(self, detail=None, code=None, errors=None):
        self.detail = self.default_detail if not detail else detail
        self.status_code = self.status_code if not code else code
        self.errors = self.errors if not errors else errors
