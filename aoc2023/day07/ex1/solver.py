import sys
from dataclasses import dataclass
from enum import Enum
from collections import Counter


class HandType(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6

    def __gt__(self, other):
        return self.value > other.value


class Card(Enum):
    _2 = 0
    _3 = 1
    _4 = 2
    _5 = 3
    _6 = 4
    _7 = 5
    _8 = 6
    _9 = 7
    _T = 8
    _J = 9
    _Q = 10
    _K = 11
    _A = 12

    def __gt__(self, other):
        return self.value > other.value


def get_hand_type(hand: list[Card]) -> HandType:
    counter = Counter(hand)

    if len(counter) == 5:
        return HandType.HIGH_CARD

    if len(counter) == 4:
        return HandType.ONE_PAIR

    if len(counter) == 3:
        for c in counter:
            if counter[c] == 3:
                return HandType.THREE_OF_A_KIND

        return HandType.TWO_PAIR

    if len(counter) == 2:
        for c in counter:
            if counter[c] == 3:
                return HandType.FULL_HOUSE

        return HandType.FOUR_OF_A_KIND

    if len(counter) == 1:
        return HandType.FIVE_OF_A_KIND

    raise ValueError("Invalid Hand")  # pragma: no cover


@dataclass
class Game:
    hand: list[Card]
    bid: int
    type: HandType

    def __gt__(self, other) -> bool:
        if self.type != other.type:
            return self.type > other.type

        for i in range(5):
            if self.hand[i] != other.hand[i]:
                return self.hand[i] > other.hand[i]

        raise ValueError("Two identical hands")  # pragma: no cover

    def __str__(self):
        return f"{[c.name for c in self.hand]} : {self.type.name}"


def parse_input(input_file: str) -> list[Game]:
    input_file = open(input_file, "r").readlines()
    games = []

    for line in input_file:
        line = line.strip().split()
        hand = [Card[f"_{c}"] for c in line[0]]
        games.append(Game(hand=hand, bid=int(line[1]), type=get_hand_type(hand)))

    return games


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/7#part1
    """
    winning = 0
    games = parse_input(input_file)
    games.sort()
    for g in games:
        print(g)
    for i, g in enumerate(games):
        winning += (i + 1) * g.bid

    return winning


if __name__ == '__main__':  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
