import sys


def parse_input(input_file: str) -> list[str]:
    with open(input_file) as f:
        inputs = f.readline().strip().split(",")
        return inputs


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/1#part1
    """
    inputs = parse_input(input_file)

    total = 0
    for input in inputs:
        nb = 0
        for letter in input:
            nb += ord(letter)
            nb *= 17
            nb = nb % 256
        total += nb
    return total


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
