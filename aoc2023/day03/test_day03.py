import day03.ex1.solver as solver_ex1

DAY = "day03"


def test_ex1_is_adjacent_symbol_same_row():
    schematic = [
        "...",
        "?..",
        "..."
    ]
    assert solver_ex1.is_part_number(schematic, 1, 1)


def test_ex1_is_adjacent_symbol_number():
    schematic = [
        "...",
        "4..",
        "..."
    ]
    assert not solver_ex1.is_part_number(schematic, 1, 1)


def test_ex1_is_adjacent_symbol_diagonal():
    schematic = [
        "..?",
        "...",
        "..."
    ]
    assert solver_ex1.is_part_number(schematic, 1, 1)


def test_ex1():
    assert solver_ex1.main(f"{DAY}/ex1/test.txt") == 4361
