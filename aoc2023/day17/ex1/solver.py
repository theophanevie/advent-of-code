import sys
from enum import Enum
from heapq import heappop, heappush
from functools import total_ordering
from dataclasses import dataclass, field
from copy import deepcopy

from typing import NamedTuple, Iterator


class Point(NamedTuple):
    y: int
    x: int


class Direction(Enum):
    NORTH = Point(-1, 0)
    SOUTH = Point(1, 0)
    EAST = Point(0, 1)
    WEST = Point(0, -1)

    def apply(self, pos: Point) -> Point:
        dy, dx = self.value
        return Point(pos.y + dy, pos.x + dx)


def possible_dir(direction: Direction | None) -> Iterator[Point]:
    if direction is None:
        yield from [Direction.SOUTH, Direction.EAST]
    if direction == Direction.NORTH or direction == Direction.SOUTH:
        yield from [Direction.EAST, Direction.WEST]
    elif direction == Direction.EAST or direction == Direction.WEST:
        yield from [Direction.SOUTH, Direction.NORTH]


@dataclass
@total_ordering
class State:
    position: Point
    previous_direction: Direction
    heat_loss: int
    path: list[Point] = field(default_factory=list)

    def __lt__(self, other):
        if not isinstance(other, State):
            return NotImplemented
        return self.heat_loss < other.heat_loss

    def futur_state(self, direction: Direction, heat_loss_map: dict[Point, int], map_size: int) -> Iterator["State"]:
        next_state = deepcopy(self)
        for _ in range(3):
            next_point = direction.apply(next_state.position)
            if not point_valid(next_point, map_size):
                break

            next_state = State(
                next_point, direction, next_state.heat_loss + heat_loss_map[next_point], next_state.path + [next_point]
            )
            yield next_state


def point_valid(pos: Point, map_size: int) -> bool:
    if pos.y < 0 or pos.y >= map_size:
        return False

    if pos.x < 0 or pos.x >= map_size:
        return False

    return True


def parse_input(input_file: str) -> tuple[dict[Point, int], int]:
    maps = {}
    with open(input_file) as f:
        for y, line in enumerate(f.readlines()):
            line = line.strip()
            for x, w in enumerate(line):
                maps[Point(y, x)] = int(w)

    return maps, x + 1


def solve(start: Point, end: Point, heat_loss_map: dict[Point, int], map_size: int) -> int:
    heap = []
    seen = set()

    heappush(heap, State(start, None, 0, [start]))

    while heap:
        state = heappop(heap)

        if (state.position, state.previous_direction) in seen:
            continue

        # print_path(state.path, map_size)
        seen.add((state.position, state.previous_direction))

        if state.position == end:
            return state.heat_loss

        for direction in possible_dir(state.previous_direction):
            for futur_state in state.futur_state(direction, heat_loss_map, map_size):
                heappush(heap, futur_state)

    assert False  # sanity check


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/1#part1
    """
    maps, map_size = parse_input(input_file)

    start = Point(0, 0)
    end = Point(map_size - 1, map_size - 1)
    return solve(start, end, maps, map_size)


def print_path(path: list[Point], map_size: int) -> None:
    print("=" * 80)
    maps = []
    for i in range(map_size):
        maps.append(["."] * map_size)

    for p in path:
        maps[p.y][p.x] = "#"

    for i in range(map_size):
        print([maps[i][j] for j in range(map_size)])


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
