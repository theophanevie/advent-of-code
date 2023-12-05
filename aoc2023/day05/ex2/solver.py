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
            if row[offset] <= x < (row[offset] + row[offset + 2]):

                # Compute the diff
                diff = x - row[offset]
                return row[offset + 1] + diff

        return x

    return map_function


def is_seed(seed: int, seeds: [int]) -> bool:
    for i in range(0, len(seeds), 2):
        if seeds[i] <= seed < seeds[i] + seeds[i + 1]:
            return True

    return False


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


def get_seed_from_location(loc: int, maps: [Callable[[int], int]]) -> int:
    tmp = loc
    for i in range(len(maps)):
        tmp = maps[- (1 + i)](tmp)

    return tmp


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/5#part2
    """
    i = 0
    seeds, maps = parse_input(input_file)

    while True:
        seed = get_seed_from_location(i, maps)
        if is_seed(seed, seeds):
            return i

        i += 1


if __name__ == '__main__':  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
