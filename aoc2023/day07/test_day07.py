import day07.ex1.solver as solver_ex1
import day07.ex2.solver as solver_ex2


DAY = "day07"

"""
EX1
"""


def test_ex1():
    assert solver_ex1.main(f"{DAY}/ex1/input.txt") == 248179786


"""
EX2
"""


def test_ex2():
    assert solver_ex2.main(f"{DAY}/ex2/input.txt") == 247885995
