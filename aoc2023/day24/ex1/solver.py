import sys
import math

UPPER_B = 400000000000000
LOWER_B = 200000000000000


class Hailstone:
    x: int
    y: int
    z: int
    dx: int
    dy: int
    dz: int
    a: float
    c: float

    def __init__(self, x, y, z, dx, dy, dz):
        self.x = x
        self.y = y
        self.z = z
        self.dx = dx
        self.dy = dy
        self.dz = dz

        self.a = self.dy / self.dx
        self.c = self.y - self.a * self.x

    def intersect(self, hs: "Hailstone") -> bool:
        # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
        # a * x + c = b * x + d ->  x = (d - c) / (a - b)

        # Check if there are parallel
        if math.isclose(self.a, hs.a):
            return False

        # Compute x, y
        x = (hs.c - self.c) / (self.a - hs.a)
        y = self.a * x + self.c
        assert math.isclose(y, hs.a * x + hs.c)

        if not (LOWER_B <= x <= UPPER_B and LOWER_B <= y <= UPPER_B):
            return False

        # Determine when they intersect
        # x = t * dx + x0
        t1 = (x - self.x) / self.dx
        assert math.isclose(t1, (y - self.y) / self.dy)

        t2 = (x - hs.x) / hs.dx
        assert math.isclose(t2, (y - hs.y) / hs.dy)

        return t1 > 0 and t2 > 0


def parse_input(input_file: str) -> list[Hailstone]:
    with open(input_file) as f:
        return [Hailstone(*list(map(int, line.replace("@", ",").split(",")))) for line in f.readlines()]


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/24#part1
    """
    stones = parse_input(input_file)

    collision_counter = 0
    for i, s1 in enumerate(stones):
        collision_counter += sum([s1.intersect(s2) for j, s2 in enumerate(stones[:i])])

    return collision_counter


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
