import sys
import math
from dataclasses import dataclass


@dataclass
class Race:
    time: int
    max_dist: int

    def get_quadratic_result(self) -> (int, int):
        """
        https://en.wikipedia.org/wiki/Quadratic_formula

        (race_time - hold_time) * hold_time > max_dist
        (race_time - hold_time) * hold_time - max_dist > 0
        race_time * hold_time  - hold_time ** 2 - max_dist > 0

        - 1 * hold_time ** 2 + race_time * hold_time - max_dist > 0

        hold_time = x
        a = -1 (constant)
        b = race_time (constant)
        d = max_dist (constant)
        """
        a = -1
        b = self.time
        c = -self.max_dist

        d = (b**2) - (4 * a * c)
        root_1 = (-b - math.sqrt(d)) / (2 * a)
        root_2 = (-b + math.sqrt(d)) / (2 * a)

        solutions = sorted([root_1, root_2])
        return math.ceil(solutions[0]), math.floor(solutions[1])


def parse_input(input_file: str) -> Race:
    input_file = open(input_file, "r")

    times = input_file.readline().strip().split()
    distances = input_file.readline().strip().split()
    tmp_time = ""
    tmp_dist = ""

    for i in range(1, len(times)):
        tmp_time += times[i]
        tmp_dist += distances[i]

    return Race(time=int(tmp_time), max_dist=int(tmp_dist))


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/6#part2
    Part1: Brute force
    Part2: Use math
    """
    lower, upper = parse_input(input_file).get_quadratic_result()
    return upper - lower + 1


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
