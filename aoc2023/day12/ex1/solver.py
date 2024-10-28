import sys
from typing import Dict, List, Any

POS = tuple[int, int]
PADDING = 1


def parse_input(input_file: str) -> dict[str, list[Any]]:
    input_file = open(input_file, "r")
    giant_field = {"rows": [], "rules": []}

    for line in input_file.readlines():
        line = line.strip().split(" ")
        giant_field["rows"].append(line[0])
        giant_field["rules"].append(line[1])

    return giant_field


def fit(j: int, row: str, rule: int) -> bool:
    if len(row[j:]) < rule:
        return False

    if j > 0 and row[j - 1] == "#":
        return False

    i = 0
    while i < rule:
        if row[j + i] == ".":
            return False
        i += 1
    if j + i < len(row) and row[j + i] == "#":
        return False

    return True


def compute_arrangements(row: str, rules: str) -> int:
    if len(rules) == 0:
        if "#" in row:
            return 0
        return 1

    rule = int(rules.split(",")[0])
    if len(row) < rule:
        return 0

    arrangements = 0
    for i in range(len(row)):
        if fit(i, row, rule):
            arrangements += compute_arrangements(row[i + rule + 1 :], rules[len(str(rule)) + 1 :])
        if row[i] == "#":
            break

    return arrangements


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/12#part1
    """

    giant_fields = parse_input(input_file)
    arrangements = 0
    for field, rules in zip(giant_fields["rows"], giant_fields["rules"]):
        arrangements += compute_arrangements(field, rules)

    return arrangements


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
