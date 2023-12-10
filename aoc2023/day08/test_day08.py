import day08.ex1.solver as solver_ex1
import day08.ex2.solver as solver_ex2

DAY = "day08"

"""
EX1
"""


def test_ex1_test_1():
    assert solver_ex1.main(f"{DAY}/ex1/test_1.txt") == 2


def test_ex1_test_2():
    assert solver_ex1.main(f"{DAY}/ex1/test_2.txt") == 6


"""
EX2
"""


def test_ex2():
    assert solver_ex2.main(f"{DAY}/ex2/test.txt") == 6
