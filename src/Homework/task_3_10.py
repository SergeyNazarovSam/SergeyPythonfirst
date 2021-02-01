# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def split_sum(s: str) -> list:
    valid_str = s.replace(',', '.')
    sum_list = valid_str.split('.')
    assert len(sum_list) == 2, f" {s} is not valid sum"
    return sum_list


def separate_to_template(value: str, template: tuple) -> dict:
    number = int(value)
    nominal_dict = {}
    for nominal in reversed(template):
        if int(number/nominal) > 0:
            nominal_dict[nominal] = int(number/nominal)
            number = number - nominal_dict[nominal]*nominal
    return nominal_dict


def show_result(ruble: dict, kopeyki: dict) -> str:
    res = ''
    for nominal in ruble:
        value = ruble[nominal]
        res = res + f' {value} of {nominal} rubles; '
    #res = res + '<br>'
    for nominal in kopeyki:
        value = kopeyki[nominal]
        res = res + f' {value} of {nominal} kopeyek; '
    return res


def solution_3_10(params: dict) -> str:
    initial_sum = params.get('initial_sum', '125.16')[0]
    res = initial_sum + ' = '
    sum_list = split_sum(initial_sum)
    ruble_template = (1, 2, 5, 10, 20, 50, 100, 200, 500)
    kopeyki_template = (1, 2, 5, 10, 20, 50)
    ruble = separate_to_template(sum_list[0], ruble_template)
    kopeyki = separate_to_template(sum_list[1], kopeyki_template)
    res = res + show_result(ruble, kopeyki)
    return res


if __name__ == '__main__':
    print(solution_3_10(input('Enter money sum \n')))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
