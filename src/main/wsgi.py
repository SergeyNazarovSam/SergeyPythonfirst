import sentry_sdk
from framework.util.settings import get_setting
from framework.dirs import DIR_SRC
from urllib.parse import parse_qs
from Homework.task_3_10 import solution_3_10

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)


def read_template(filename: str) -> str:
    tempate_dir = DIR_SRC / 'main' / 'template'
    template = tempate_dir / filename
    assert template.is_file()       # check if file exists
    with template.open('r') as file_index:
        content = file_index.read()
    return content


def show_environ(environ: dict) -> str:
    environ_nice = ''
    for key in environ:
        value = environ[key]
        environ_nice += f'{key} = {value} <br>'
    return environ_nice


def raise_error(environ: dict) -> str:
    res = 'param /e/ found in path'
    return res


def empty_res (in_value: dict) -> str:
    return ''


def application(environ, start_response):


    qsi = parse_qs(environ["QUERY_STRING"])

    task_list = {
        '/': ('index.html', empty_res, '200 OK', 'Title of page', {}),
        '/e/': ('basic.html', raise_error, '500 Internal Server Error', 'Error on the page', {}),
        '/environ': ('environ.html', show_environ, '200 OK', 'Show environ variable', environ),
        '/tasks/task_3_10': ('basic.html', solution_3_10, '200 OK', 'Task should return nominals of incoming value', qsi)
    }

    template, solution, status, title, input_dict = task_list.get(environ['PATH_INFO'],
                                                                  ('Index.html', empty_res, '404 Not Found', 'Check the path, please', {}))


    headers = {
        "Content-type": "text/html",
    }


    html_body = read_template(template)
    res = solution(input_dict)
    html_body = html_body.format(title=title, result=res)

    payload = html_body.encode()


    start_response(status, list(headers.items()))

    yield payload
