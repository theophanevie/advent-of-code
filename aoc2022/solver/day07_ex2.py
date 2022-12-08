import sys

from solver.day07_ex1 import compute_fs

FS_SIZE = 70000000
SIZE_NEEDED = 30000000


def dir_to_delete(filename: str) -> int:
    dir_size = []
    fs = compute_fs(filename, dir_size)

    dir_size.sort()
    free_space = FS_SIZE - dir_size[-1]

    print(f"{free_space=}")
    for size in dir_size:
        print(f"{size=}")
        if size + free_space >= SIZE_NEEDED:
            return size

    raise ValueError("Should never happened")


if __name__ == "__main__":
    print(dir_to_delete(sys.argv[1]))
