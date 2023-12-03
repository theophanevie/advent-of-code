import sys
import re

IS_NOT_A_SYMBOL = r"([0-9]|\.)"


def reader(input_file: str) -> [str]:
    input_file = open(input_file, "r").readlines()

    return [line.strip() for line in input_file]


def is_part_number(schematic: [str], y: int, x: int) -> bool:
    # Check is there is any symbol adjacent to a given  x, y
    # [ (y - 1, x - 1), (y - 1, x), (y - 1, x + 1)
    # [ (y, x - 1), (y, x), (y, x + 1)
    # [ (y + 1, x - 1), (y + 1, x), (y + 1, x + 1)

    def test_x_axis(b: int, a: int):
        if a > 0:
            if not re.match(IS_NOT_A_SYMBOL, schematic[b][a - 1]):
                return True

        if not re.match(IS_NOT_A_SYMBOL, schematic[b][a]):
            return True

        if a < len(schematic[0]) - 1:
            if not re.match(IS_NOT_A_SYMBOL, schematic[b][a + 1]):
                return True

        return False

    if y > 0:
        if test_x_axis(y - 1, x):
            return True

    if test_x_axis(y, x):
        return True

    if y < len(schematic) - 1:
        if test_x_axis(y + 1, x):
            return True

    return False


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/3#part1
    """
    schematic = reader(input_file)
    valid_part_sum = 0

    for y in range(len(schematic)):
        number_buffer = ""
        valid_part_number = False

        for x in range(len(schematic[y])):
            if schematic[y][x].isdigit():
                number_buffer += schematic[y][x]
                if not valid_part_number:
                    valid_part_number = is_part_number(schematic, y, x)

            else:
                if valid_part_number:
                    valid_part_sum += int(number_buffer)
                valid_part_number = False
                number_buffer = ""

        if valid_part_number:
            valid_part_sum += int(number_buffer)

    return valid_part_sum


if __name__ == '__main__':  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
