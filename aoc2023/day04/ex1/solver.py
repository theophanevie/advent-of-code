import sys
import re

CARD_GAME = r"Card([ 0-9]+):([0-9 ]+)\|([0-9 ]+)"


def reader(input_file: str) -> [str]:
    input_file = open(input_file, "r").readlines()
    cards = []

    for line in input_file:
        card_game_re = re.match(CARD_GAME, line)
        cards.append(
            (
                card_game_re.group(1),
                list(filter(lambda a: a != "", card_game_re.group(2).split(" "))),
                list(filter(lambda a: a != "", card_game_re.group(3).split(" "))),
            )
        )

    return cards


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/4#part1
    """
    cards_points = []

    for card in reader(input_file):
        good_number = 0
        for number in card[1]:
            if number in card[2]:
                good_number += 1

        if good_number:
            cards_points.append(pow(2, good_number - 1))

    return sum(cards_points)


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
