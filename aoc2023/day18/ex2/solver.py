import sys
from enum import Enum
from typing import NamedTuple


def parse_input(input_file: str) -> list[list[str]]:
    instructions = []
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip().split(" ")
            instructions.append([line[2][2:-2], line[2][-2]])

    return instructions


class Point(NamedTuple):
    x: int
    y: int

class Direction(Enum):
    NORTH = Point(-1, 0)
    SOUTH = Point(1, 0)
    EAST = Point(0, 1)
    WEST = Point(0, -1)

    def apply(self, pos: Point, duration: int) -> Point:
        dx, dy = self.value
        return Point(pos.x + dx * duration, pos.y + dy * duration)


def construct_points(instructions: list[list[str]]) -> tuple[list[Point], int]:
    line_length = 0
    points = [Point(0, 0)]
    for instruction in instructions:
        line_len = int(instruction[0], 16)
        line_length += line_len
        match instruction[1]:
            case "3":
                points.append(Direction.NORTH.apply(points[-1], line_len))
            case "1":
                points.append(Direction.SOUTH.apply(points[-1], line_len))
            case "0":
                points.append(Direction.EAST.apply(points[-1], line_len))
            case "2":
                points.append(Direction.WEST.apply(points[-1], line_len))

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
