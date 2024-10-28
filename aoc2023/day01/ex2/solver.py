import string
import sys

# Since eight-two is meant to be understood as 82, we can't replace all the letters with the number.
# The maximum number of letters that can be reused from one digit to another is 1, so we need to keep the first and
# last letters.
DIGIT_AS_LETTERS = [
    ("one", "o1e"),
    ("two", "t2o"),
    ("three", "t3e"),
    ("four", "f4r"),
    ("five", "f5e"),
    ("six", "s6x"),
    ("seven", "s7n"),
    ("eight", "e8t"),
    ("nine", "n9e"),
]


def reader(input_file: str) -> str:
    input_file = open(input_file, "r").readlines()
    for line in input_file:
        for search, replace in DIGIT_AS_LETTERS:
            line = line.replace(search, replace)
        yield line.strip(string.ascii_lowercase + "\n")


def main(input_file: str) -> int:
    return sum([int(line[0] + line[-1]) for line in reader(input_file)])


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
