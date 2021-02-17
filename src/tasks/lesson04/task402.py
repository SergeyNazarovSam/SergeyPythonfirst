import os
from pathlib import Path
from typing import Optional

from typed_ast._ast3 import keyword

from framework.dirs import DIR_STORAGE
from main.custom_types import RequestT
from main.custom_types import ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson04/task402.html"
TEMPLATE2 = "tasks/lesson04/task402_2.html"


def handler(request: RequestT) -> ResponseT:
    headers = {}
    #client_name = get_client(request)
    #if not client_name:
    client_name = create_new_client(request)
    headers["Set-Cookie"] = f"name={client_name}"

    client_data = request.query.get("number", "0")[0]
    result = "invalid input"
    if client_data == "stop":
        result = calc_sum(client_name, request.path)
        context = {
            "number": result,
            "summa": f'Сумма всех накопленных чисел: {result}',
        }
    elif client_data.isnumeric():
        number = int(client_data)
        result = add_number(client_name, number, request.path)
        context = {
            "number": result,
            "summa": f'Последнее добавленное число: {result}',
        }
    if request.path == "/tasks/4/402/":
        document = render_template(TEMPLATE, context)
    else:
        document = render_template(TEMPLATE2, context)

    response = ResponseT(
        headers=headers,
        payload=str(document),
    )

    return response


def create_new_client(request: RequestT) -> str:
    return f"{request.user_name}_{request.comp_name}"


def get_client_file(client_name: str) -> Path:
    file_path = DIR_STORAGE / f"{client_name}.txt"

    return file_path


def calc_sum(client_name: str, key_filter: str) -> int:
    data_file = get_client_file(client_name)

    with data_file.open("r") as src:
        result = 0
        for line in src.readlines():
            key_val = eval(line.strip())
            result = result + key_val.get(key_filter, 0)
    return result


def add_number(client_name: str, number: int, key_filter: str) -> int:
    data_file = get_client_file(client_name)
    data_line = {key_filter: number}
    with data_file.open("a") as dst:
        dst.write(str(data_line)+"\n")

    return number


def get_client(request: RequestT) -> Optional[str]:
    cookies = request.headers.get("Cookie")
    if not cookies:
        return None

    cookies = cookies.replace(" ", "")
    cookies = cookies.replace(";", "=")
    cookies_list = cookies.split("=")
    cookies_dict = {}
    for index in range(0, len(cookies_list) - 1):
        if index % 2 == 0:
            cookies_dict[cookies_list[index]] = cookies_list[index+1]
    cookie_value = cookies_dict.get("name")
    return cookie_value or None
