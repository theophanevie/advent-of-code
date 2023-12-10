import day10.ex1.solver as solver_ex1
# import day09.ex2.solver as solver_ex2

DAY = "day10"

"""
EX1
"""


def test_ex1_test_simple():
    assert solver_ex1.main(f"{DAY}/ex1/test_1.txt") == 4


def test_ex1_test_medium():
    assert solver_ex1.main(f"{DAY}/ex1/test_2.txt") == 8


"""
EX2
"""


# def test_ex2():
#     assert solver_ex2.main(f"{DAY}/ex2/test.txt") == 2
