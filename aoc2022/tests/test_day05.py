from solver.day05_ex1 import compute_new_stacks


def test_day2_ex1():
    assert compute_new_stacks("inputs/input_day05_0") == 'CMZ'
    assert compute_new_stacks("inputs/input_day05_1") == "GRTSWNJHH"


def test_day2_ex2():
    assert compute_new_stacks("inputs/input_day05_0", crane_9001=True) == "MCD"
    assert compute_new_stacks("inputs/input_day05_1", crane_9001=True) == "QLFQDBBHM"
