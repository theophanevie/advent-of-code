import sys
import re
from pydantic import BaseModel


class MyHashMap(BaseModel):
    _buckets = list[list[str | int]]

    def __init__(self, /, **data: any):
        super().__init__(**data)
        self._buckets = [[] for _ in range(512)]

    def _my_hash(self, label: str) -> int:
        res = 0

        for letter in label:
            res += ord(letter)
            res *= 17
            res = res % 256

        return res

    def set_value(self, label: str, value: int) -> None:
        pos = self._my_hash(label) * 2
        if label in self._buckets[pos + 1]:
            index = self._buckets[pos + 1].index(label)
            self._buckets[pos][index] = value
        else:
            self._buckets[pos].append(value)
            self._buckets[pos + 1].append(label)

    def delete_value(self, label: str) -> None:
        pos = self._my_hash(label) * 2
        if label not in self._buckets[pos + 1]:
            return

        index = self._buckets[pos + 1].index(label)
        self._buckets[pos].pop(index)
        self._buckets[pos + 1].pop(index)

    def get_value(self, label: str) -> str | int:
        pos = self._my_hash(label) * 2
        index = self._buckets[pos + 1].index(label)
        return self._buckets[pos][index]

    def compute_score(self) -> int:
        score = 0

        for i in range(256):
            for j, value in enumerate(self._buckets[i * 2]):
                score += (i + 1) * (j + 1) * value

        return score

    def print(self) -> None:
        for i in range(256):
            for j, value in enumerate(self._buckets[i * 2]):
                print(f"{i=}, {value=}, {self._buckets[i * 2 + 1][j]}")


def parse_input(input_file: str) -> list[str]:
    with open(input_file) as f:
        inputs = f.readline().strip().split(",")
        return inputs


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/15#part2
    """
    inputs = parse_input(input_file)
    my_hash_map = MyHashMap()

    for input in inputs:
        input_re = re.match(r"([a-z]+)(-|=[0-9]+)", input)
        label = input_re.group(1)

        match input_re.group(2)[0]:
            case "-":
                my_hash_map.delete_value(label)
            case "=":
                my_hash_map.set_value(label, int(input_re.group(2)[1]))
            case _:
                raise ValueError(f"Invalid input: {input}")

    return my_hash_map.compute_score()


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
