import pytest
from Homework.task_3_10 import solution_3_10


@pytest.mark.unit
def test_3_10_calculation():
    res = solution_3_10({'initial_sum': ['123.15']})
    assert res.replace(' ', '') == '123.15=1of100rubles;1of20rubles;1of2rubles;1of1rubles;1of10kopeyek;1of5kopeyek;', 'Calculation of nominals failed 123.15'
    res = solution_3_10({'initial_sum': ['100.00']})
    assert res.replace(' ', '') == '100.00=1of100rubles;', 'Calculation of nominals failed 100.00'