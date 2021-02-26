from random import randint

from django.http import HttpRequest, HttpResponse

from main.custom_types import RequestT
from main.custom_types import ResponseT
from main.util import render_template

TEMPLATE = "index.html"


def handler(_request: RequestT) -> ResponseT:
    context = {"random_number": randint(100000, 999999)}

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

    return response


def handler_django(_req: HttpRequest) -> HttpResponse:
    context = {"random_number": randint(100000, 999999)}

    document = render_template(TEMPLATE, context)

    response = HttpResponse(document)

    return response
