import sys
import math
from dataclasses import dataclass

import sympy

UPPER_B = 400000000000000
LOWER_B = 200000000000000

@dataclass
class Hailstone:
    x: int
    y: int
    z: int
    dx: int
    dy: int
    dz: int


def parse_input(input_file: str) -> list[Hailstone]:
    with open(input_file) as f:
        return [Hailstone(*list(map(int, line.replace("@", ",").split(",")))) for line in f.readlines()]


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/24#part2
    """
    hailstones = parse_input(input_file)

    """
    for a rock : x, y, z, dx, dy, dz and a hailstone : hsx, hsy, hsz, hsdx, hsdy, hsdz to interset at t
    
    for x coordinate (it is the same for y and z):
    ---> x + t * dx == hsx + hsdx * t 
    <==> t * (hsdx - dx) == x - hsx 
    <==> t == (x - hsx) / (hsdx - dx)
    
    (x - hsx) / (hsdx - dx) == (y - hsy) / (hsdy - dy)
    <==> (x - hsx) * (hsdy - dy) == (y - hsy) * (hsdx - dx)
    """

    x, y, z, dx, dy, dz = sympy.symbols("x, y, z, dx, dy, dz")
    eqs = []
    for hs in hailstones[:4]: # Only need number of coordinates + 1
        eqs.append((x - hs.x) * (hs.dy - dy) - (y - hs.y) * (hs.dx - dx))
        eqs.append((x - hs.x) * (hs.dz - dz) - (z - hs.z) * (hs.dx - dx))

    return sympy.solve(eqs)[0][x] + sympy.solve(eqs)[0][y] + sympy.solve(eqs)[0][z]



if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
