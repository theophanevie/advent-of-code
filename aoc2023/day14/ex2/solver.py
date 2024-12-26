import sys
from collections import OrderedDict
from copy import deepcopy

POS = tuple[int, int]
PLATFORM = dict[POS, str]
CYCLE = 1_000_000_000


def print_platform(height: int, width: int, platform: PLATFORM) -> None:
    for i in range(height):
        print("".join([platform[(j, i)] for j in range(width)]))


def parse_input(input_file: str) -> tuple[int, int, PLATFORM]:
    platform = {}
    with open(input_file, "r") as f:
        for i, line in enumerate([line.strip() for line in f.readlines()]):
            for j, case in enumerate(line):
                platform[(j, i)] = case

    return i + 1, j + 1, platform


def moove(offset: POS, old_pos: POS, platform: PLATFORM) -> PLATFORM:
    x, y = old_pos
    off_x, off_y = offset
    new_pos = x + off_x, y + off_y

    if new_pos in platform and platform[new_pos] == ".":
        platform[new_pos] = "O"
        platform[old_pos] = "."
        platform = moove(offset, new_pos, platform)

    return platform


def perform_cycle(height: int, width: int, platform: PLATFORM) -> PLATFORM:
    # North
    for i in range(width):
        for j in range(height):
            pos = i, j
            if platform[pos] == "O":
                platform = moove((0, -1), pos, platform)

    # WEST
    for j in range(height):
        for i in range(width):
            pos = i, j
            if platform[pos] == "O":
                platform = moove((-1, 0), pos, platform)

    # SOUTH
    for i in range(width):
        for j in range(height - 1, -1, -1):
            pos = i, j
            if platform[pos] == "O":
                platform = moove((0, 1), pos, platform)

    # EAST
    for i in range(width - 1, -1, -1):
        for j in range(height):
            pos = i, j
            if platform[pos] == "O":
                platform = moove((1, 0), pos, platform)

    return platform


def compute_score(height: int, width: int, platform: PLATFORM) -> int:
    score = 0
    for j in range(width):
        for i in range(height):
            if platform[(j, i)] == "O":
                score += height - i

    return score


def platform_to_string(height: int, width: int, platform: PLATFORM) -> str:
    as_str = ""
    for i in range(height):
        for j in range(width):
            as_str += platform[(j, i)]

    return as_str


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/14#part2
    """

    height, width, platform = parse_input(input_file)
    intermediate_res = OrderedDict()

    for cycle_nb in range(CYCLE):
        platform = perform_cycle(height, width, platform)
        platform_as_str = platform_to_string(height, width, platform)

        if platform_as_str in intermediate_res:
            break

        intermediate_res[platform_as_str] = deepcopy(platform)

    i = list(intermediate_res.keys()).index(platform_as_str)
    remaining_cycle = (CYCLE - (cycle_nb + 1)) % (len(intermediate_res) - i)
    final_platform_str = list(intermediate_res.keys())[i + remaining_cycle]
    final_platform = intermediate_res[final_platform_str]

    return compute_score(height, width, final_platform)


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
