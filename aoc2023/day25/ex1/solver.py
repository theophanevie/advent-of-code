import sys
from collections import defaultdict
import copy
from random import choice
from uuid import uuid4


def parse_input(input_file: str) -> dict[str, list[str]]:
    jump_table = defaultdict(set)
    with open(input_file) as f:
        for line in f.readlines():
            nodes = line.replace(":", "").split()
            jump_table[nodes[0]] = jump_table[nodes[0]].union(set(nodes[1:]))
            for node in nodes[1:]:
                jump_table[node].add(nodes[0])

    return {node: list(jump_table[node]) for node in jump_table}


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/25#part1

    https://en.m.wikipedia.org/wiki/Minimum_cut
    https://en.m.wikipedia.org/wiki/Karger%27s_algorithm
    """
    jump_table_ori = parse_input(input_file)

    jump_table = copy.deepcopy(jump_table_ori)
    components = {node: {node} for node in jump_table}

    while not len(jump_table[list(jump_table.keys())[0]]) == 3:

        jump_table = copy.deepcopy(jump_table_ori)
        components = {node: {node} for node in jump_table}
        while len(components) > 2:
            edge = choice([(node, target) for node in jump_table for target in jump_table[node]])

            new_n = str(uuid4())
            components[new_n] = components[edge[0]] | components[edge[1]]

            # Assemble new table and remove ref to itself
            jump_table[new_n] = list(filter(lambda x: x not in edge, jump_table[edge[0]] + jump_table[edge[1]]))


            for node in edge:
                # Remove outdated node
                del jump_table[node]
                del components[node]

                # Update ref to deleted node
                for n in jump_table.keys():
                    for _ in range(jump_table[n].count(node)):
                        jump_table[n].remove(node)
                        jump_table[n].append(new_n)


    return len(list(components.values())[0]) * len(list(components.values())[1])



if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
