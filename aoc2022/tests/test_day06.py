from solver.day06_ex1 import packet_start_pos


def test_day06_ex1():
    assert packet_start_pos("inputs/input_day06_0", 4) == 5
    assert packet_start_pos("inputs/input_day06_1", 4) == 10
    assert packet_start_pos("inputs/input_day06_2", 4) == 6
    assert packet_start_pos("inputs/input_day06_3", 4) == 1658


def test_day06_ex2():
    assert packet_start_pos("inputs/input_day06_0", 14) == 23
    assert packet_start_pos("inputs/input_day06_1", 14) == 29
    assert packet_start_pos("inputs/input_day06_2", 14) == 23
    assert packet_start_pos("inputs/input_day06_3", 14) == 2260
