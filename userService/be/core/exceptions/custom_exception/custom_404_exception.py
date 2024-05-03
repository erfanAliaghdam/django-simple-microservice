from rest_framework.exceptions import APIException
from rest_framework import status


class Custom404Exception(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Item not found."

    def __init__(self, detail=None, code=None, item_name=None):
        self.detail = self.default_detail if not detail else detail
        self.status_code = self.status_code if not code else code
        if item_name:
            self.default_detail = f"{item_name} not found."
