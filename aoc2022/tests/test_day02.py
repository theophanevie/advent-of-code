from solver.day02_ex1 import compute_strategy_score as compute_strategy_score_ex1
from solver.day02_ex2 import compute_strategy_score as compute_strategy_score_ex2


def test_day2_ex1():
    assert compute_strategy_score_ex1("inputs/input_day02_0") == 15
    assert compute_strategy_score_ex1("inputs/input_day02_1") == 10310


def test_day2_ex2():
    assert compute_strategy_score_ex2("inputs/input_day02_0") == 12
    assert compute_strategy_score_ex2("inputs/input_day02_1") == 14859
