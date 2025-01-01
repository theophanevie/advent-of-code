import sys
import re
from collections.abc import Callable
from dataclasses import dataclass


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int


@dataclass
class Workflow:
    slug: str
    rules: list[Callable[[Part], str | None]]

    def evaluation(self, part: Part) -> str:
        print(f"WF {self.slug}")
        for rule in self.rules:
            res = rule(part)
            if res is None:
                continue
            return res

        assert False  # Sanity check


def parse_input(input_file: str) -> tuple[dict[str, Workflow], list[Part]]:
    workflows = {}
    parts = []

    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()

            if line == "":
                continue

            # Part
            if mp := re.match(r"{x=([0-9]+),m=([0-9]+),a=([0-9]+),s=([0-9]+)}", line):
                parts.append(Part(x=int(mp.group(1)), m=int(mp.group(2)), a=int(mp.group(3)), s=int(mp.group(4))))
                continue

            # Workflow
            if mw := re.match(r"([a-z]+)\{([a-z0-9><:,AR]+)}", line):
                rules = []
                for rule in mw.group(2).split(","):
                    if mr := re.match(r"([xmas])([<>])([0-9]+):([a-zAR]+)", rule):
                        if mr.group(2) == "<":
                            # capture mr.group(...) values as default arguments to avoid scope issues due to Python closures.
                            rules.append(
                                lambda part,
                                w_slug=mr.group(4),
                                part_attr=mr.group(1),
                                threshold=int(mr.group(3)): w_slug if getattr(part, part_attr) < threshold else None
                            )
                        elif mr.group(2) == ">":
                            # capture mr.group(...) values as default arguments to avoid scope issues due to Python closures.
                            rules.append(
                                lambda part,
                                w_slug=mr.group(4),
                                part_attr=mr.group(1),
                                threshold=int(mr.group(3)): w_slug if getattr(part, part_attr) > threshold else None
                            )
                    else:
                        # capture mr.group(...) values as default arguments to avoid scope issues due to Python closures.
                        rules.append(lambda _, r=rule: r)

                workflows[mw.group(1)] = Workflow(slug=mw.group(1), rules=rules)
                continue

            assert False  # Sanity check

    return workflows, parts


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/X#part1
    """
    accepted_parts = 0

    worflows, parts = parse_input(input_file)
    for part in parts:
        print(f"========> {part}")
        res = worflows["in"].evaluation(part)
        while res not in ["A", "R"]:
            res = worflows[res].evaluation(part)

        if res == "A":
            accepted_parts += part.x + part.a + part.m + part.s

    return accepted_parts


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
