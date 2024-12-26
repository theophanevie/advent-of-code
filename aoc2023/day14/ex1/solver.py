import sys

POS = tuple[int, int]
PLATFORM = dict[POS, str]


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


def tilt(height: int, width: int, platform: PLATFORM) -> PLATFORM:
    for i in range(width):
        for j in range(height):
            pos = i, j
            if platform[pos] == "O":
                platform = moove((0, -1), pos, platform)

    return platform


def compute_score(height: int, width: int, platform: PLATFORM) -> int:
    score = 0
    for j in range(width):
        for i in range(height):
            if platform[(j, i)] == "O":
                score += height - i

    return score


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/14#part1
    """

    height, width, platform = parse_input(input_file)
    platform = tilt(height, width, platform)
    return compute_score(height, width, platform)


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
