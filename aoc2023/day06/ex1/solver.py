import sys
from math import prod
from dataclasses import dataclass


@dataclass
class Race:
    time: int
    max_dist: int

    def get_dist(self, hold_time: int) -> int:
        return (self.time - hold_time) * hold_time

    def get_winning_hold_times(self) -> [int]:
        winning_hold_times = []
        for i in range(self.time):
            if self.get_dist(i) > self.max_dist:
                winning_hold_times.append(i)

        return winning_hold_times


def parse_input(input_file: str) -> [Race]:
    input_file = open(input_file, "r")
    races = []

    times = input_file.readline().strip().split()
    distances = input_file.readline().strip().split()
    for i in range(1, len(times)):
        races.append(Race(time=int(times[i]), max_dist=int(distances[i])))

    return races


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/6#part1
    Part1: Brute force
    Part2: Use math
    """
    possible_win = []
    for race in parse_input(input_file):
        possible_win.append(len(race.get_winning_hold_times()))

    return prod(possible_win)


if __name__ == '__main__':  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
