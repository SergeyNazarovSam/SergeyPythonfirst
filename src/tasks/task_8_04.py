from Types.custom_type import RequestT


def validate_list(s: str) -> list:
    valid_str = s.replace(' ', '')
    return valid_str


def extend_dict(result_dict: dict, new_int: list) -> dict:
    return_dict = result_dict
    for key in new_int:
        if return_dict.get(key, 'fail') == 'fail':
            return_dict[key] = 1
        else:
            return_dict[key] = return_dict[key] + 1
    return return_dict


def show_result(result_dict: dict) -> str:
    res = str(result_dict)
    return res


def solution_8_04(req: RequestT) -> str:
    initial_list = req.new_data.get('initial_list', '1,2,3')[0]
    num_list = validate_list(initial_list)
    num_list = num_list.split(',')
    int_list = list(int(e) for e in num_list)
    result_dict = req.previous_data
    result_dict = extend_dict(result_dict, int_list)
    res = show_result(result_dict)
    return res


if __name__ == '__main__':
    input_str = '1'
    result_dict = {}
    while True:
        input_str = input('Enter list of values \n')
        if input_str == '':
            break
        new_list = validate_list(input_str)
        req = RequestT(new_data={'initial_list': [new_list]}, previous_data=result_dict)
        res = solution_8_04(req)
        print(res)
        result_dict = eval(res)