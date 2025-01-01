import sys


def parse_input(input_file: str) -> list[str]:
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()

    return []


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/X#part1
    """
    inputs = parse_input(input_file)

    return 0


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
