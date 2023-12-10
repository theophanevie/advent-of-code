import day10.ex1.solver as solver_ex1
import day10.ex2.solver as solver_ex2

DAY = "day10"

"""
EX1
"""


def test_ex1_test_1():
    assert solver_ex1.main(f"{DAY}/ex1/test_1.txt") == 4


def test_ex1_test_2():
    assert solver_ex1.main(f"{DAY}/ex1/test_2.txt") == 8


"""
EX2
"""


def test_ex2_test_1():
    assert solver_ex2.main(f"{DAY}/ex2/test_1.txt") == 1


def test_ex2_test_2():
    assert solver_ex2.main(f"{DAY}/ex2/test_2.txt") == 4


def test_ex2_test_3():
    assert solver_ex2.main(f"{DAY}/ex2/test_3.txt") == 8


def test_ex2_test_4():
    assert solver_ex2.main(f"{DAY}/ex2/test_4.txt") == 10


def test_ex2_test_5():
    assert solver_ex2.main(f"{DAY}/ex2/test_5.txt") == 15
