import day09.ex1.solver as solver_ex1
import day09.ex2.solver as solver_ex2

DAY = "day09"

"""
EX1
"""


def test_ex1_test_1():
    assert solver_ex1.main(f"{DAY}/ex1/test.txt") == 114


def test_next_read_simple_1():
    assert solver_ex1.compute_next(solver_ex1.compute_pyramid([10, 13, 16, 21, 30, 45])) == 68


def test_next_read_simple_2():
    assert solver_ex1.compute_next(solver_ex1.compute_pyramid([1, 3, 6, 10, 15, 21])) == 28


"""
EX2
"""


def test_ex2():
    assert solver_ex2.main(f"{DAY}/ex2/test.txt") == 2
