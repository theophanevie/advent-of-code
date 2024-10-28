import day05.ex1.solver as solver_ex1
import day05.ex2.solver as solver_ex2


DAY = "day05"

"""
EX1
"""


def test_get_seed_location_one_by_one():
    """
    Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82
    """
    _, maps = solver_ex1.parse_input(f"{DAY}/ex1/test.txt")

    assert maps[0](79) == 81
    assert maps[1](81) == 81
    assert maps[2](81) == 81
    assert maps[3](81) == 74
    assert maps[4](74) == 78
    assert maps[5](78) == 78
    assert maps[6](78) == 82


def test_get_seed_location():
    _, maps = solver_ex1.parse_input(f"{DAY}/ex1/test.txt")

    assert solver_ex1.get_seed_location(79, maps) == 82
    assert solver_ex1.get_seed_location(14, maps) == 43
    assert solver_ex1.get_seed_location(55, maps) == 86
    assert solver_ex1.get_seed_location(13, maps) == 35


def test_ex1():
    assert solver_ex1.main(f"{DAY}/ex1/test.txt") == 35


"""
EX2
"""


def test_get_seed_from_location_one_by_one():
    """
    Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82
    """
    _, maps = solver_ex2.parse_input(f"{DAY}/ex2/test.txt")
    maps.reverse()

    assert maps[0](35) == 35
    assert maps[1](35) == 34
    assert maps[2](34) == 34
    assert maps[3](34) == 41
    assert maps[4](41) == 52
    assert maps[5](52) == 13
    assert maps[6](13) == 13


def test_get_seed_from_location():
    _, maps = solver_ex2.parse_input(f"{DAY}/ex2/test.txt")

    assert solver_ex2.get_seed_from_location(35, maps) == 13
    assert solver_ex2.get_seed_from_location(82, maps) == 79
    assert solver_ex2.get_seed_from_location(43, maps) == 14
    assert solver_ex2.get_seed_from_location(86, maps) == 55
    assert solver_ex2.get_seed_from_location(46, maps) == 82


def test_ex2():
    assert solver_ex2.main(f"{DAY}/ex2/test.txt") == 46
