import sys
import re
from dataclasses import dataclass


@dataclass
class Card:
    draw_numbers: list[str]
    winning_numbers: list[str]
    occurrences: int = 1
    

CARD_GAME = r"Card([ 0-9]+):([0-9 ]+)\|([0-9 ]+)"


def parse_input(input_file: str) -> dict[int, Card]:
    input_file = open(input_file, "r").readlines()
    cards = {}

    for line in input_file:
        card_game_re = re.match(CARD_GAME, line)
        cards[int(card_game_re.group(1).strip())] = Card(
            list(filter(lambda a: a != "", card_game_re.group(2).split(" "))),
            list(filter(lambda a: a != "", card_game_re.group(3).split(" ")))
        )

    return cards


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/4#part2
    """
    cards = parse_input(input_file)

    for i in range(1, len(cards.values()) + 1):
        good_number = 0
        for number in cards[i].draw_numbers:
            if number in cards[i].winning_numbers:
                good_number += 1

        for j in range(1, good_number + 1):
            cards[i + j].occurrences += cards[i].occurrences

    return sum([card.occurrences for card in cards.values()])


if __name__ == '__main__':  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
