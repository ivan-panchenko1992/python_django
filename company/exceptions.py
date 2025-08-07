from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        if isinstance(exc, TypeError):
            return Response(
                {
                    "error": "Wrong Data",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {
                "error": "Something went wrong",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response