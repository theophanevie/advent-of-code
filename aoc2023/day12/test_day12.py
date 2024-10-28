import day12.ex1.solver as solver_ex1
import day12.ex2.solver as solver_ex2

DAY = "day12"

"""
EX1
"""


def test_ex1_test_fine():
    assert solver_ex1.compute_arrangements("?###????????", "3,2,1") == 10


def test_ex1_test_complex():
    assert solver_ex1.compute_arrangements("#????????.#?#??????", "2,1,1,5,1") == 36


def test_ex1_test_full():
    assert solver_ex1.main(f"{DAY}/ex1/test.txt") == 21


"""
EX2
"""


def test_ex2_test_full():
    assert solver_ex2.main(f"{DAY}/ex2/test.txt") == 525152
