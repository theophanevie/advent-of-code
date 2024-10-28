import string
import sys


def reader(input_file: str) -> str:
    input_file = open(input_file, "r").readlines()
    for line in input_file:
        yield line.strip(string.ascii_lowercase + "\n")


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/1#part1
    """
    return sum([int(line[0] + line[-1]) for line in reader(input_file)])


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
