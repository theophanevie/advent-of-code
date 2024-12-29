import sys
from enum import Enum
from typing import NamedTuple


def parse_input(input_file: str) -> list[list[str]]:
    instructions = []
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip().split(" ")
            instructions.append([line[0], line[1]])

    return instructions


class Point(NamedTuple):
    x: int
    y: int

class Direction(Enum):
    NORTH = Point(-1, 0)
    SOUTH = Point(1, 0)
    EAST = Point(0, 1)
    WEST = Point(0, -1)

    def apply(self, pos: Point) -> Point:
        dx, dy = self.value
        return Point(pos.x + dx, pos.y + dy)


def construct_points(instructions: list[list[str]]) -> tuple[list[Point], int]:
    def multiple_apply(direction: Direction, start: Point, iteration: int) -> Point:
        for _ in range(iteration):
            start = direction.apply(start)
        return start

    line_length = 0
    points = [Point(0, 0)]
    for instruction in instructions:
        line_len = int(instruction[1])
        line_length += line_len
        match instruction[0]:
            case "U":
                points.append(multiple_apply(Direction.NORTH, points[-1], line_len))
            case "D":
                points.append(multiple_apply(Direction.SOUTH, points[-1], line_len))
            case "R":
                points.append(multiple_apply(Direction.EAST, points[-1], line_len))
            case "L":
                points.append(multiple_apply(Direction.WEST, points[-1], line_len))

    return points, line_length


def get_area(points: list[Point]) -> float:
    """
    https://en.wikipedia.org/wiki/Shoelace_formula
    """
    points.append(points[0])
    formula = 0
    for i in range(len(points) - 1):
        formula += (points[i].y + points[i].y) * (points[i].x - points[i + 1].x)

    # adding -1 to get positive answer as 0,0 is top left
    return -1 * 0.5 * formula


def get_points_inside(points_nb: int, area: int) -> float:
    """
    https://en.wikipedia.org/wiki/Pick%27s_theorem
    """
    return -1 * (- area + points_nb / 2 - 1)

def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/1#part1
    """
    instructions = parse_input(input_file)
    points, points_nb = construct_points(instructions)
    area  = get_area(points)
    res = get_points_inside(points_nb, int(area))
    return int(res) + points_nb


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
