import day06.ex1.solver as solver_ex1
import day06.ex2.solver as solver_ex2

DAY = "day06"

"""
EX1
"""


def test_ex1():
    assert solver_ex1.main(f"{DAY}/ex1/test.txt") == 288


"""
EX2
"""


def test_ex2():
    assert solver_ex2.main(f"{DAY}/ex2/test.txt") == 71503
