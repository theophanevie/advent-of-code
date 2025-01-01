import sys
import re
from collections.abc import Iterator
from copy import copy
from dataclasses import dataclass


@dataclass
class Part:
    x: list[int]
    m: list[int]
    a: list[int]
    s: list[int]

    def possibilities(self) -> int:
        return len(self.x) * len(self.m) * len(self.a) * len(self.s)


@dataclass
class Rule:
    follow_up: str
    threshold: int | None = None
    operator: str | None = None
    part_attribute: str | None = None


@dataclass
class Workflow:
    slug: str
    rules: list[Rule]

    def evaluation(self, part: Part) -> Iterator[str, Part]:
        for rule in self.rules:
            if rule.operator is None:
                yield (rule.follow_up, part)
                continue

            value = getattr(part, rule.part_attribute)
            validating, not_validating = [], []
            for elt in value:
                # ugly but quicker ...
                if eval(f"{elt} {rule.operator} {rule.threshold}"):
                    validating.append(elt)
                else:
                    not_validating.append(elt)

            new_part = copy(part)
            setattr(new_part, rule.part_attribute, validating)
            yield (rule.follow_up, new_part)
            setattr(part, rule.part_attribute, not_validating)


def parse_input(input_file: str) -> dict[str, Workflow]:
    workflows = {}

    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()

            if mw := re.match(r"([a-z]+)\{([a-z0-9><:,AR]+)}", line):
                rules = []
                for rule in mw.group(2).split(","):
                    if mr := re.match(r"([xmas])([<>])([0-9]+):([a-zAR]+)", rule):
                        rules.append(
                            Rule(
                                threshold=int(mr.group(3)),
                                part_attribute=mr.group(1),
                                follow_up=mr.group(4),
                                operator=mr.group(2),
                            )
                        )
                    else:
                        rules.append(Rule(follow_up=rule))

                workflows[mw.group(1)] = Workflow(slug=mw.group(1), rules=rules)
                continue

            if line == "":
                # discard "Parts" part of the input
                break

            assert False  # Sanity check

    return workflows


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/X#part1
    """

    def eval_workflows(start_slug: str, start_part: Part, workflows: dict[str, Workflow]) -> list[Part]:
        parts = []
        for slug, part in workflows[start_slug].evaluation(start_part):
            if slug == "R":
                continue

            if slug == "A":
                parts.append(part)
                continue

            parts += eval_workflows(slug, part, workflows)
        return parts

    workflows = parse_input(input_file)
    start = Part(
        x=[i for i in range(1, 4001)],
        m=[i for i in range(1, 4001)],
        a=[i for i in range(1, 4001)],
        s=[i for i in range(1, 4001)],
    )
    parts = eval_workflows("in", start, workflows)

    return sum([part.possibilities() for part in parts])


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
