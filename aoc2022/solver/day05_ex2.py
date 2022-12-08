import sys

from solver.day05_ex1 import compute_new_stacks

if __name__ == "__main__":
    print(compute_new_stacks(sys.argv[1], crane_9001=True))
