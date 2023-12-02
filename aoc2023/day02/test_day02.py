from day02.ex1.solver import main as main_ex1
from day02.ex2.solver import main as main_ex2

DAY = "day02"


def test_ex1():
    assert main_ex1(f"{DAY}/ex1/test.txt") == 8


def test_ex2():
    assert main_ex2(f"{DAY}/ex2/test.txt") == 2286
