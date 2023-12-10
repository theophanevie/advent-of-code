import sys


def parse_input(input_file: str) -> tuple[dict[tuple[int, int], str], tuple[int, int]]:
    input_file = open(input_file, "r")
    grid = {}

    for y, line in enumerate(input_file.readlines()):
        line = line.strip()
        for x, pipe in enumerate(line):
            grid[x, y] = pipe

            if pipe == "S":
                start_pos = (x, y)

    return grid, start_pos


def find_next(grid: dict[tuple[int, int], str], cur_pos: tuple[int, int], from_pos: tuple[int, int]) \
        -> tuple[int, int] | None:
    deltas = []

    match grid[cur_pos]:

        case "|":
            deltas = [(0, -1), (0, 1)]

        case "-":
            deltas = [(-1, 0), (1, 0)]

        case "L":
            deltas = [(0, -1), (1, 0)]

        case "J":
            deltas = [(0, -1), (-1, 0)]

        case "7":
            deltas = [(0, 1), (-1, 0)]

        case "F":
            deltas = [(0, 1), (1, 0)]

    # Dead end !
    if len(deltas) == 0:
        print("")
        return None

    first_exit = tuple(map(lambda x, y: x + y, cur_pos, deltas[0]))
    second_exit = tuple(map(lambda x, y: x + y, cur_pos, deltas[1]))
    if first_exit == from_pos:
        return second_exit
    if second_exit == from_pos:
        return first_exit

    # Invalid jump !
    return None


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/7#part1
    """
    # Large input
    sys.setrecursionlimit(25_000)

    grid, start_pos = parse_input(input_file)

    def pipe_explorer(seen: list[tuple[int, int]], cur_pos: tuple[int, int] | None, from_pos: tuple[int, int]) -> int:

        if cur_pos in seen:
            return len(seen)

        if cur_pos is None:
            return -1

        seen.append(cur_pos)
        return pipe_explorer(seen, find_next(grid, cur_pos, from_pos), cur_pos)

    return max(pipe_explorer([start_pos], (start_pos[0], start_pos[1] + 1), start_pos),
               pipe_explorer([start_pos], (start_pos[0] + 1, start_pos[1]), start_pos),
               pipe_explorer([start_pos], (start_pos[0], start_pos[1] - 1), start_pos),
               pipe_explorer([start_pos], (start_pos[0] - 1, start_pos[1]), start_pos)) // 2


if __name__ == '__main__':  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
