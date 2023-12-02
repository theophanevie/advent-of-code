import sys
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Dir:
    name: str
    size: int = 0
    children: list["Dir"] = field(default_factory=lambda: [])
    parent: Optional["Dir"] = None


def handle_instruction(line: list[str], dir: Dir) -> Dir:
    if line[0] != "$":
        raise Exception("Invalid prompt")

    if line[1] == "ls":
        return dir

    if line[1] != "cd":
        raise ValueError("Command is not supported")

    if line[2] == "..":
        return dir.parent

    children = Dir(line[2])
    dir.children.append(children)
    children.parent = dir

    return children


def compute_fs(filename: str, dir_size: list[int]) -> Dir:
    scripts_output = [line.strip().split(" ") for line in open(filename, "r").readlines()]

    # Init root
    scripts_output = scripts_output[1:]
    root = Dir(name="/")

    cur_dir = root
    for line in scripts_output:

        match line[0]:

            case "$":
                cur_dir = handle_instruction(line, cur_dir)

            case "dir":
                pass

            case _:
                cur_dir.size += int(line[0])

    def size(dir: Dir) -> int:
        if len(dir.children) == 0:
            dir_size.append(dir.size)
            return dir.size

        dir.size += sum([size(children) for children in dir.children])
        dir_size.append(dir.size)
        return dir.size

    size(root)
    return root


def to_delete(filename: str) -> int:
    dir_size = []
    fs = compute_fs(filename, dir_size)

    dir_size.sort()
    for i in range(1, len(dir_size)):
        if dir_size[i] >= 100000:
            return sum(dir_size[:i])

    raise ValueError("Invalid input fs")
