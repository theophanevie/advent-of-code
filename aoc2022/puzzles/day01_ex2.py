import sys
from itertools import groupby


def compute_max_cal(filename: str) -> int:

    list_snack = open(filename, "r").readlines()
    elves_cal = [
        sum([int(snack_cal) for snack_cal in list(elf_snacks_cal)])
        for match, elf_snacks_cal in groupby(list_snack, lambda x: x != "\n")
        if match
    ]

    elves_cal.sort()
    return sum(elves_cal[-3:])


if __name__ == "__main__":
    print(compute_max_cal(sys.argv[1]))
