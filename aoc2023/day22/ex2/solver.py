import sys
from collections import deque
from typing import Iterator


def parse_input(input_file: str) -> Iterator[list[int]]:
    with open(input_file) as f:
        for line in f.readlines():
            yield list(map(int, line.replace("~", ",").split(",")))


def overlap(brick1: list[int], brick2: list[int]) -> bool:
    return max(brick1[0], brick2[0]) <= min(brick1[3], brick2[3]) and max(brick1[1], brick2[1]) <= min(brick1[4], brick2[4])


def pack_down_bricks(bricks: list[list[int]]) -> None:
    for i in range(len(bricks)):
        new_z = 1
        for packed in bricks[:i]:
            if overlap(bricks[i], packed):
                new_z = max(new_z, packed[5] + 1)

        bricks[i][5] = new_z + bricks[i][5] - bricks[i][2]
        bricks[i][2] = new_z


def compute_neighbors(bricks: list[list[int]]) -> tuple[dict[int, set[int]], dict[int, set[int]]]:
    x_supports_b = {i: set() for i in range(len(bricks))}
    x_is_supported_by_b = {i: set() for i in range(len(bricks))}
    for i in range(len(bricks)):
        for j in range(i + 1, len(bricks)):
            if overlap(bricks[i], bricks[j]) and bricks[i][5] + 1 == bricks[j][2]:
                x_supports_b[i].add(j)
                x_is_supported_by_b[j].add(i)

    return x_supports_b, x_is_supported_by_b


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/22#part1
    """
    bricks = list(parse_input(input_file))
    bricks.sort(key=lambda brick: brick[2]) # sort on distance to the ground

    pack_down_bricks(bricks)
    bricks.sort(key=lambda brick: brick[2])

    x_supports_b, x_is_supported_by_b = compute_neighbors(bricks)

    total = 0
    for i in range(len(bricks)):
        q = deque(x_supports_b[i])
        falling = {i}

        while q:
            b = q.popleft()

            if x_is_supported_by_b[b] <= falling:
                falling.add(b)
                q.extend(x_supports_b[b])

        total += len(falling) - 1

    return total


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
