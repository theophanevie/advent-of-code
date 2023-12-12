import day11.ex1.solver as solver_ex1
import day11.ex2.solver as solver_ex2

DAY = "day11"

"""
EX1
"""


def test_ex1_test_fine():
    universe, galaxies = solver_ex1.parse_input(f"{DAY}/ex1/test.txt")

    # expend the universe and get new galaxy pos
    galaxies = solver_ex1.expend_galaxies(universe, galaxies)

    distance = solver_ex1.dist_from_galaxies(list(galaxies.values()))

    assert len(distance) == 36
    assert distance[(4, 0), (9, 10)] == 15
    assert distance[(0, 2), (12, 7)] == 17
    assert distance[(0, 11), (5, 11)] == 5


def test_ex1_test_full():
    assert solver_ex1.main(f"{DAY}/ex1/test.txt") == 374


"""
EX2
"""


def test_ex2_test_full():
    solver_ex2.PADDING = 1
    assert solver_ex2.main(f"{DAY}/ex2/test.txt") == 374
    solver_ex2.PADDING = 9
    assert solver_ex2.main(f"{DAY}/ex2/test.txt") == 1030
    solver_ex2.PADDING = 99
    assert solver_ex2.main(f"{DAY}/ex2/test.txt") == 8410
