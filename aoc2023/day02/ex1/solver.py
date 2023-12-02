import re
import sys

CUBE_INPUT = r"(\d+) ([a-z]+)"
GAME_REGEX = r"Game (\d+): (.*)"


def reader(input_file: str) -> [(int, [dict[str, int]])]:
    input_file = open(input_file, "r").readlines()

    for line in input_file:
        game_re = re.match(GAME_REGEX, line)
        game_nb = int(game_re.group(1))
        game_combinations = []

        for raw_cube_inputs in game_re.group(2).split(";"):
            cube_inputs = {"green": 0, "blue": 0, "red": 0}
            for rcube_input in re.finditer(CUBE_INPUT, raw_cube_inputs):
                cube_inputs[rcube_input.group(2)] = int(rcube_input.group(1))

            game_combinations.append(cube_inputs)

        yield game_nb, game_combinations


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/2#part1
    """
    rule = {"green": 13, "blue": 14, "red": 12}
    possible_games = 0

    def is_possible(combinations: [dict[str, int]]) -> bool:
        for combination in combinations:
            for key in rule:
                # Check whether several cubes of this color have been displayed during a combination of this game.
                if combination[key] > rule[key]:
                    return False
        return True

    for game_nb, game_combinations in reader(input_file):
        if is_possible(game_combinations):
            possible_games += game_nb

    return possible_games


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
