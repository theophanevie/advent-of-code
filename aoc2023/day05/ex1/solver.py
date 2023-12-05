import sys
from collections.abc import Callable
import re

RE_SEEDS = r"seeds: ([0-9 ]+)"
RE_MAP = r"([a-z\- :]+)\n(([0-9 ]+\n)+)"


def create_map_function(row: [int]) -> Callable[[int], int]:
    """
    Create a function computing the destination for the list of input "row"
    """
    def map_function(x: int) -> int:
        for offset in range(0, len(row), 3):
            # Check if the number is within start and start + max range
            if row[offset + 1] <= x < (row[offset + 1] + row[offset + 2]):

                # Compute the diff
                diff = row[offset + 0] - row[offset + 1]
                return x + diff

        return x

    return map_function


def parse_input(input_file: str) -> ([str], [Callable[[int], int]]):
    input_file = open(input_file, "r").read()

    seeds = [int(s) for s in re.match(RE_SEEDS, input_file).group(1).split()]
    maps = []

    # For each x-to-x map
    for g in re.finditer(RE_MAP, input_file):
        row = [int(x) for x in g.group(2).split()]

        # Append to the list the function computing source -> dest
        maps.append(create_map_function(row))

    return seeds, maps


def get_seed_location(seed: int, maps: [Callable[[int], int]]) -> int:
    tmp = seed

    for map_function in maps:
        tmp = map_function(tmp)

    return tmp


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/5#part1
    """
    seeds, maps = parse_input(input_file)
    return min([get_seed_location(seed, maps) for seed in seeds])


if __name__ == '__main__':  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
