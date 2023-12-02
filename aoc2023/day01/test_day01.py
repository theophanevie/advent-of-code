from day01.ex1.solver import main as main_ex1
from day01.ex2.solver import main as main_ex2

DAY = "day01"


def test_ex1():
    assert main_ex1(f"{DAY}/ex1/test.txt") == 142


def test_ex2():
    assert main_ex2(f"{DAY}/ex2/test.txt") == 281
