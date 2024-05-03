from rest_framework.views import exception_handler
from rest_framework.response import Response
from core.exceptions import (
    Custom400Exception,
    Custom401Exception,
    Custom403Exception,
    Custom404Exception,
    Custom500Exception,
    Custom412Exception,
)


def custom_exception_handler(exc, context):
    custom_exceptions = (
        Custom400Exception,
        Custom401Exception,
        Custom403Exception,
        Custom404Exception,
        Custom500Exception,
        Custom412Exception,
    )

    if isinstance(exc, custom_exceptions):
        response = {
            "status": "failed",
            "message": exc.detail,
            "data": {"errors": exc.errors}
            if hasattr(exc, "errors") and exc.errors is not None
            else [],
        }
        return Response(response, status=exc.status_code)
    else:
        return exception_handler(exc, context)
