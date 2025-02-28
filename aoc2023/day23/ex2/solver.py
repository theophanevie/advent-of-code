import queue
import sys
from collections import deque, defaultdict

POS = tuple[int, int]

def parse_input(input_file: str) -> list[str]:
    with open(input_file) as f:
        return [line.strip() for line in f.readlines()]


def find_junctions(grid: list[str]) -> set[POS]:
    junctions = set()
    size = len(grid)

    for y in range(size):
        for x in range(size):
            if grid[y][x] == "#":
                continue

            neighbour_count = 0
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + dx < size and 0 <= y + dy < size and grid[y + dy][x + dx] != "#":
                    neighbour_count += 1

            if neighbour_count > 2:
                junctions.add((y, x))

    return junctions


def compute_jump_map(junctions: set[POS], grid: list[str]) -> dict[POS, dict[POS, int]]:
    jump_map = defaultdict(dict)
    size = len(grid)

    for pos in junctions:
        q = deque({(*pos, 0)})
        seen = set()

        while q:
            y, x, path_len = q.popleft()
            seen.add((y, x))

            if (y, x) != pos and (y, x) in junctions:
                jump_map[pos][(y, x)] = path_len
                continue

            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + dx < size and 0 <= y + dy < size and grid[y + dy][x + dx] != "#" and (y + dy, x + dx) not in seen:
                    q.append((y + dy, x + dx, path_len + 1))

    return jump_map


def find_paths(jump_map: dict[POS, dict[POS, int]], start: POS, end: POS) -> list[list[POS]]:
    paths = []
    q = deque([(start, [start])])

    while q:
        pos, path = q.popleft()

        if pos == end:
            paths.append(path)
            continue

        for p in jump_map[pos].keys():
            if p not in path:
                q.append((p, path + [p]))

    return paths


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/X#part1
    """
    grid = parse_input(input_file)

    assert len(grid[0]) == len(grid)

    start_y, start_x = 0, grid[0].index('.')
    end_y, end_x = len(grid) - 1, grid[-1].index('.')

    junctions = find_junctions(grid).union({(start_y, start_x), (end_y, end_x)})

    jump_map = compute_jump_map(junctions, grid)

    paths = find_paths(jump_map, (start_y, start_x), (end_y, end_x))

    longest_path = 0
    for path in paths:
        longest_path = max(longest_path, sum([jump_map[p1][p2] for p1, p2 in zip(path, path[1:])]))

    return longest_path


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
