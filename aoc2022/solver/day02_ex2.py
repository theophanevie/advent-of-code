import sys

points = {
    "A": 0,
    "B": 1,
    "C": 2,
}


def compute_round_score(opponent: int, strategy: str) -> int:
    # point given for the play minus 1 (easier for math) + 1 (point subtracted) + result of the match

    if strategy == "Y":
        return opponent + 1 + 3

    if strategy == "X":
        return (opponent - 1) % 3 + 1 + 0

    if strategy == "Z":
        return (opponent + 1) % 3 + 1 + 6

    raise ValueError("Invalid play")


def compute_strategy_score(filename: str) -> int:
    strategy = [line.strip().split(" ") for line in open(filename, "r").readlines()]
    strategy_score = 0

    for cur_round in strategy:
        strategy_score += compute_round_score(points[cur_round[0]], cur_round[1])

    return strategy_score


if __name__ == "__main__":
    print(compute_strategy_score(sys.argv[1]))
