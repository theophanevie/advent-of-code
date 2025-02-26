import sys
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum


STEPS = 6

class Direction(Enum):
    NORTH = (1, 0)
    SOUTH = (-1, 0)
    WEST = (0, 1)
    EAST = (0, -1)


@dataclass
class Position:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))

    def move(self, direction: Direction) -> "Position":
        return Position(self.y + direction.value[0], self.x + direction.value[1])


def parse_input(input_file: str) -> tuple[dict[Position, str], Position]:
    grid = {}
    start_pos = None
    with open(input_file) as f:
        for y, line in enumerate(f.readlines()):
            for x, val in enumerate(line.strip()):
                grid[Position(x, y)] = val
                if val == "S":
                    start_pos = Position(x, y)

    return grid, start_pos


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/21#part1
    """
    grid, start_pos = parse_input(input_file)
    seen = defaultdict(set)

    def move(pos: Position, path_len: int) -> None:
        if pos not in grid or grid[pos] == "#":
            return
        if path_len == STEPS + 1 or pos in seen[path_len]:
            return

        seen[path_len].add(pos)
        for d in Direction:
            move(pos.move(d), path_len + 1)

    move(start_pos, 0)

    # Off by one but why ?
    return len(seen[STEPS])


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
