import sys


def parse_input(input_file: str) -> list[tuple[list[str], list[str]]]:
    line_patterns = []
    with open(input_file) as f:
        line_pattern = []
        for line in [line.strip() for line in f.readlines()]:
            if not line:
                line_patterns.append(line_pattern)
                line_pattern = []
                continue

            line_pattern.append("".join(["0" if cur == "." else "1" for cur in line]))

        line_patterns.append(line_pattern)

    patterns = []
    for line_pattern in line_patterns:
        col_pattern = []
        for i in range(len(line_pattern[0])):
            col_pattern.append("".join(["0" if pattern[i] == "0" else "1" for pattern in line_pattern]))

        patterns.append((line_pattern, col_pattern))

    return patterns


def is_refection(i: int, pattern: list[str]) -> bool:
    offset = 1
    bit_smudged = False
    while i + offset < len(pattern) and i + 1 - offset >= 0:
        xor = int(pattern[i + offset], 2) ^ int(pattern[i + 1 - offset], 2)
        if bin(xor).count("1") > 1:
            return False

        if bin(xor).count("1") == 1:
            if bit_smudged:
                return False
            bit_smudged = True

        offset += 1
    return bit_smudged


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/13#part1
    """

    patterns = parse_input(input_file)
    score = 0
    for pattern in patterns:
        line_pattern, col_pattern = pattern

        for i in range(len(line_pattern) - 1):
            if is_refection(i, line_pattern):
                score += (i + 1) * 100

        for i in range(len(col_pattern) - 1):
            if is_refection(i, col_pattern):
                score += i + 1
    return score


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
