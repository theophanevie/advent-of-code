import sys
from dataclasses import dataclass
from collections import deque
from enum import Enum


class Direction(Enum):
    NORTH = (1, 0)
    SOUTH = (-1, 0)
    WEST = (0, 1)
    EAST = (0, -1)


@dataclass
class Position:
    y: int
    x: int

    def __hash__(self):
        return hash((self.y, self.x))

    def move(self, direction: Direction) -> "Position":
        return Position(self.y + direction.value[0], self.x + direction.value[1])


def parse_input(input_file: str) -> tuple[dict[Position, str], Position, int]:
    grid = {}
    start_pos = None
    with open(input_file) as f:
        for y, line in enumerate(f.readlines()):
            for x, val in enumerate(line.strip()):
                grid[Position(y, x)] = val
                if val == "S":
                    start_pos = Position(y, x)

    grid_size = max([pos.y for pos in grid.keys()]) + 1
    return grid, start_pos, grid_size


def print_grid(grid: dict[Position, str], positions: set[Position], grid_size: int) -> None:
    for y in range(grid_size):
        line = ""
        for x in range(grid_size):
            if Position(y, x) in positions:
                line += "0"
            else:
                line += grid[Position(y, x)]
        print(line)


def compute_garden_plot(grid: dict[Position, str], start_pos: Position, steps: int, grid_size: int) -> set[Position]:
    seen = set()
    answer = set()
    q = deque([(start_pos, 0)])

    while len(q):
        pos, cur_step = q.popleft()

        new_p = Position(pos.y % grid_size, pos.x % grid_size)
        if new_p not in grid or grid[new_p] == "#" or cur_step == steps + 1 or pos in seen:
            continue

        if cur_step % 2 == steps % 2: # tile can only be access on odd or even occ
            answer.add(pos)

        seen.add(pos)
        for d in Direction:
            q.append((pos.move(d), cur_step + 1))

    return answer


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/21#part2
    """
    grid, start_pos, grid_size = parse_input(input_file)



    res = []
    for x in range(4):
        steps = start_pos.x + 2 * grid_size * x
        res.append(len(compute_garden_plot(grid, start_pos, steps, grid_size)))


    fd = [b - a for a, b in zip(res, res[1:])]
    sd = [b - a for a, b in zip(fd, fd[1:])]

    assert sd[0] == sd[1]

    # We have a quadratic function, GG!
    # Manually compute a, b, and c, then run Python to evaluate f(steps / 2 * grid_size).

    # Thanks to https://www.youtube.com/watch?v=C5wYxR6ZAPM and https://github.com/villuna/aoc23/wiki/A-Geometric-solution-to-advent-of-code-2023,-day-21
    # for the excellent explanations!
    # The geometric approach was also quite interesting: https://www.youtube.com/watch?v=9UOMZSL0JTg&list=PLnNm9syGLD3zLoIGWeHfnEekEKxPKLivw&index=27

    print(res)
    return 0


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
