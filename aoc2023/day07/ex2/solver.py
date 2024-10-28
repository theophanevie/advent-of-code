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
    _J = 0
    _2 = 1
    _3 = 2
    _4 = 3
    _5 = 4
    _6 = 5
    _7 = 6
    _8 = 7
    _9 = 8
    _T = 9
    _Q = 10
    _K = 11
    _A = 12

    def __gt__(self, other):
        return self.value > other.value


def get_hand_type(hand: list[Card]) -> HandType:
    counter = Counter(hand)

    if len(counter) == 5:
        if Card["_J"] not in counter:
            return HandType.HIGH_CARD
        return HandType.ONE_PAIR

    if len(counter) == 4:
        if Card["_J"] in counter:
            return HandType.THREE_OF_A_KIND
        return HandType.ONE_PAIR

    if len(counter) == 3:
        # Nb of occ of the most common elt
        if counter.most_common()[0][1] == 3:
            if Card["_J"] in counter:
                return HandType.FOUR_OF_A_KIND
            return HandType.THREE_OF_A_KIND

        if Card["_J"] in counter:
            if counter[Card["_J"]] == 2:
                return HandType.FOUR_OF_A_KIND
            return HandType.FULL_HOUSE
        return HandType.TWO_PAIR

    if len(counter) == 2:
        if Card["_J"] in counter:
            return HandType.FIVE_OF_A_KIND

        # Nb of occ of the most common elt
        if counter.most_common()[0][1] == 3:
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

    def __str__(self):  # pragma: no cover
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
    games = parse_input(input_file)
    games.sort()

    return sum(i * g.bid for i, g in enumerate(games, start=1))


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
