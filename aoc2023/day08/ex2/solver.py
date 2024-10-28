import sys
from dataclasses import dataclass, field
import re
from math import lcm
from typing import Any


NODE_RE = r"([A-Z0-9]+) = \(([A-Z0-9]+), ([A-Z0-9]+)\)"


@dataclass
class Node:
    label: str
    right: Any | None = None
    left: Any | None = None
    moves_to_z: list[str] = field(default_factory=list)

    def __str__(self) -> str:  # pragma: no cover
        return (
            f"[{self.label}] "
            f"r->{self.right.label if self.right else None}, "
            f"l->{self.left.label if self.left else None}, "
            f"Z_dist->{self.moves_to_z}"
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


def dist_to_z_node(start_node: Node, instructions: str) -> int:
    i = 0
    node = start_node
    instructions_len = len(instructions)

    while True:
        if node.label[-1] == "Z":
            return i

        if instructions[i % instructions_len] == "R":
            node = node.right

        elif instructions[i % instructions_len] == "L":
            node = node.left

        i += 1


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/7#part1
    """
    instructions, nodes = parse_input(input_file)
    dist_to_z = []

    for label in nodes:
        if label[-1] != "A":
            continue

        dist_to_z.append(dist_to_z_node(nodes[label], instructions))

    return lcm(*dist_to_z)


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
