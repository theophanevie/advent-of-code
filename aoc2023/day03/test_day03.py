import day03.ex1.solver as solver_ex1
import day03.ex2.solver as solver_ex2

DAY = "day03"

"""
EX1
"""


def test_ex1_is_adjacent_symbol_same_row():
    schematic = ["...", "?..", "..."]
    assert solver_ex1.is_part_number(schematic, 1, 1)


def test_ex1_is_adjacent_symbol_number():
    schematic = ["...", "4..", "..."]
    assert not solver_ex1.is_part_number(schematic, 1, 1)


def test_ex1_is_adjacent_symbol_diagonal():
    schematic = ["..?", "...", "..."]
    assert solver_ex1.is_part_number(schematic, 1, 1)


def test_ex1():
    assert solver_ex1.main(f"{DAY}/ex1/test.txt") == 4361


def test_ex1_full_input():
    assert solver_ex1.main(f"{DAY}/ex1/input.txt") == 517021


"""
EX2
"""


def test_ex2_gear_coord_two():
    schematic = ["..*", ".4.", ".*."]
    assert solver_ex2.find_gears(schematic, 1, 1) == [(0, 2), (2, 1)]


def test_ex2_gear_engine_parts():
    schematic = ["..*", ".4.", ".*."]
    assert dict(solver_ex2.get_gears_engine_parts(schematic)) == {(0, 2): [4], (2, 1): [4]}


def test_ex2():
    assert solver_ex2.main(f"{DAY}/ex2/test.txt") == 467835


def test_ex2_full_input():
    assert solver_ex2.main(f"{DAY}/ex2/input.txt") == 81296995
