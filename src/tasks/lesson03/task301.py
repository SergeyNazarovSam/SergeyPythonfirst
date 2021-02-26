from django.http import HttpRequest, HttpResponse

from main.custom_types import RequestT
from main.custom_types import ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson03/task301.html"


def handler(request: RequestT) -> ResponseT:
    name = request.query.get("name", [""])[0]

    context = {
        "input_name": name,
        "greeting_name": name or "anonymous",
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

    return response


def handler_django(request: HttpRequest) -> HttpResponse:
    name = request.GET.get("name", "")

    context = {
        "input_name": name,
        "greeting_name": name or "anonymous",
    }

    document = render_template(TEMPLATE, context)

    response = HttpResponse(document)

    return response
