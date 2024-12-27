import sys
from collections import deque
from collections.abc import Iterator


COORD = tuple[int, int]


def parse_input(input_file: str) -> list[str]:
    with open(input_file) as f:
        contraption = [line.strip() for line in f.readlines()]

    return contraption


def compute_delta(delta: COORD, tile: str) -> Iterator[COORD]:
    match tile:
        case ".":
            yield delta

        case "-" if delta[0] == 0:
            yield delta

        case "-":
            yield from ((0, -1), (0, 1))

        case "|" if delta[1] == 0:
            yield delta

        case "|":
            yield from ((-1, 0), (1, 0))

        case "/":
            yield -delta[1], -delta[0]

        case "\\":
            yield delta[1], delta[0]


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/1#part1
    """
    contraption = parse_input(input_file)
    width = len(contraption)

    def compute(start_pos: tuple[COORD, COORD]) -> int:
        energized = set()
        history = set()
        q = deque()
        q.append(start_pos)

        while len(q):
            delta, cur_pos = q.popleft()
            history.add((delta, cur_pos))
            energized.add(cur_pos)

            for d in compute_delta(delta, contraption[cur_pos[0]][cur_pos[1]]):
                new_pos = (cur_pos[0] + d[0], cur_pos[1] + d[1])

                if 0 > new_pos[0] or new_pos[0] >= width or 0 > new_pos[1] or new_pos[1] >= width:
                    continue

                if (d, new_pos) in history:
                    continue

                q.append((d, new_pos))

        return len(energized)

    return compute(((0, 1), (0, 0)))


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
