import sentry_sdk
from os import getenv
from framework.util.settings import get_setting

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)

def application(environ, start_response):
    if environ["PATH_INFO"] == "/e/":
        division = 1 / 0

    aPathStr = getenv("Path")

    status = "200 OK"

    headers = {
        "Content-type": "text/html",
    }

    aHtmlBody = (
        "<!DOCTYPE html>"
        "<html>"
        "<head>"
        "<title>Test project</title>"
        '<meta charset="utf-8">'
        "</head>"
        "<body>"
        "<h1>Sergey first project</h1>"
        "<hr>"
        "<p>Path variable:</p>"
        "<p>{PathStr}</p>"
        "<p>Environ variable:</p>"
        "<p>{environ}</p>"
        "</body>"
        "</html>"
    )
    aHtmlBody = aHtmlBody.format(PathStr=aPathStr, environ=environ)

    payload = aHtmlBody.encode()

    start_response(status, list(headers.items()))

    yield payload
