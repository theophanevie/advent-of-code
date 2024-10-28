import re
import sys
from functools import reduce

CUBE_INPUT = r"(\d+) ([a-z]+)"
GAME_REGEX = r"Game (\d+): (.*)"


def reader(input_file: str) -> [(int, dict[str, int])]:
    input_file = open(input_file, "r").readlines()

    for line in input_file:
        game_re = re.match(GAME_REGEX, line)
        game_nb = int(game_re.group(1))

        cube_inputs = {"green": 0, "blue": 0, "red": 0}
        for raw_cube_inputs in game_re.group(2).split(";"):
            for rcube_input in re.finditer(CUBE_INPUT, raw_cube_inputs):
                if cube_inputs[rcube_input.group(2)] < int(rcube_input.group(1)):
                    cube_inputs[rcube_input.group(2)] = int(rcube_input.group(1))

        yield game_nb, cube_inputs


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/2#part2
    """
    result = []

    for game_nb, game_combinations in reader(input_file):
        result.append(reduce(lambda x, y: x * y, [val for val in game_combinations.values()]))

    return sum(result)


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
