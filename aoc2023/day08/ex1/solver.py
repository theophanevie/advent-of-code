import sys
from dataclasses import dataclass
import re
from typing import Any


NODE_RE = r"([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)"


@dataclass
class Node:
    label: str
    right: Any | None = None
    left: Any | None = None

    def __str__(self):  # pragma: no cover
        return (
            f"[{self.label}] "
            f"r->{self.right.label if self.right else None} "
            f"l->{self.left.label if self.left else None}"
        )


def parse_input(input_file: str) -> tuple[str, dict[str, Node]]:
    input_file = open(input_file, "r")

    instructions = input_file.readline().strip()
    nodes = {}

    input_file.readline()
    for line in input_file.readlines():
        match = re.match(NODE_RE, line)

        for i in range(1, 4):
            if match.group(i) not in nodes:
                nodes[match.group(i)] = Node(label=match.group(i))

        nodes[match.group(1)].left = nodes[match.group(2)]
        nodes[match.group(1)].right = nodes[match.group(3)]

    return instructions, nodes


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/7#part1
    """
    instructions, nodes = parse_input(input_file)

    i = 0
    node = nodes["AAA"]
    instructions_len = len(instructions)

    while True:
        if node.label == "ZZZ":
            return i

        if instructions[i % instructions_len] == "R":
            node = node.right

        elif instructions[i % instructions_len] == "L":
            node = node.left

        i += 1


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
