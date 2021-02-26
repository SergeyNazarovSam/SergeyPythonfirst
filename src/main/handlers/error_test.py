from http import HTTPStatus

from django.http import HttpRequest, HttpResponse

from main.custom_types import RequestT
from main.custom_types import ResponseT


def handler(_request: RequestT) -> ResponseT:
    payload = str(1 / 0)

    response = ResponseT(
        payload=payload,
        status=HTTPStatus.INTERNAL_SERVER_ERROR,
    )

    return response


def handler_django(_request: HttpRequest) -> HttpResponse:
    payload = str(1 / 0)

    response = HttpResponse(payload)
    response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR

    return response
