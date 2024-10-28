import sys

POS = tuple[int, int]


def parse_input(input_file: str) -> tuple[dict[POS, str], POS]:
    input_file = open(input_file, "r")
    grid = {}

    for y, line in enumerate(input_file.readlines()):
        line = line.strip()
        for x, pipe in enumerate(line):
            grid[x, y] = pipe

            if pipe == "S":
                start_pos = (x, y)

    return grid, start_pos


def find_next(grid: dict[POS, str], cur_pos: POS, from_pos: POS) -> POS | None:
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
        return None

    first_exit = tuple(map(lambda x, y: x + y, cur_pos, deltas[0]))
    second_exit = tuple(map(lambda x, y: x + y, cur_pos, deltas[1]))
    if first_exit == from_pos:
        return second_exit
    if second_exit == from_pos:
        return first_exit

    # Invalid jump !
    return None


def find_loop(grid: dict[POS, str], start_pos: POS) -> list[POS]:
    def pipe_explorer(seen: list[POS], cur_pos: POS | None, from_pos: POS) -> list[POS]:
        if cur_pos in seen:
            return seen

        if cur_pos is None:
            return []

        seen.append(cur_pos)
        return pipe_explorer(seen, find_next(grid, cur_pos, from_pos), cur_pos)

    return max(
        pipe_explorer([start_pos], (start_pos[0], start_pos[1] + 1), start_pos),
        pipe_explorer([start_pos], (start_pos[0] + 1, start_pos[1]), start_pos),
        pipe_explorer([start_pos], (start_pos[0], start_pos[1] - 1), start_pos),
        pipe_explorer([start_pos], (start_pos[0] - 1, start_pos[1]), start_pos),
        key=lambda x: len(x),
    )


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/7#part1
    """
    # Large input
    sys.setrecursionlimit(25_000)
    possible_nest = set()

    grid, start_pos = parse_input(input_file)
    loop = find_loop(grid, start_pos)

    for y in range(max(pos[1] for pos in grid.keys())):
        inside = False
        prev_turn = ""

        for x in range(max(pos[0] for pos in grid.keys())):
            if (x, y) in loop:
                if grid[x, y] in "7FSJL":
                    if prev_turn == "":
                        prev_turn = grid[x, y]
                    else:
                        if (prev_turn in "JSL" and grid[x, y] in "7F") or (prev_turn in "7F" and grid[x, y] in "SJL"):
                            inside = not inside

                        prev_turn = ""

                if grid[x, y] == "|":
                    inside = not inside

            else:
                if inside:
                    possible_nest.add((x, y))

    return len(possible_nest)


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
