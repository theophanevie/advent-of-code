import sys
from collections import defaultdict


def reader(input_file: str) -> [str]:
    input_file = open(input_file, "r").readlines()

    return [line.strip() for line in input_file]


def find_gears(schematic: [str], y: int, x: int) -> [(int, int)]:
    # Check is there is any symbol adjacent to a given  x, y
    # [ (y - 1, x - 1), (y - 1, x), (y - 1, x + 1)
    # [ (y, x - 1), (y, x), (y, x + 1)
    # [ (y + 1, x - 1), (y + 1, x), (y + 1, x + 1)
    gear_coordinates = []

    def test_x_axis(b: int, a: int):
        if a > 0:
            if "*" == schematic[b][a - 1]:
                gear_coordinates.append((b, a - 1))

        if "*" == schematic[b][a]:
            gear_coordinates.append((b, a))

        if a < len(schematic[0]) - 1:
            if "*" == schematic[b][a + 1]:
                gear_coordinates.append((b, a + 1))

        return None

    if y > 0:
        test_x_axis(y - 1, x)

    test_x_axis(y, x)

    if y < len(schematic) - 1:
        test_x_axis(y + 1, x)

    return gear_coordinates



def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/3#part1
    """
    schematic = reader(input_file)
    gears = defaultdict(list)

    for y in range(len(schematic)):
        number_buffer = ""
        found_gears = set()

        for x in range(len(schematic[y])):
            if schematic[y][x].isdigit():
                number_buffer += schematic[y][x]
                found_gears |= set(find_gears(schematic, y, x))

            elif len(number_buffer):
                number = int(number_buffer)
                for gear_coord in found_gears:
                    gears[gear_coord].append(number)

                found_gears = set()
                number_buffer = ""

        if len(number_buffer):
            number = int(number_buffer)
            for gear_coord in found_gears:
                gears[gear_coord].append(number)

    gear_ratios = []
    for engine_parts in gears.values():
        if len(engine_parts) == 2:
            gear_ratios.append(engine_parts[0] * engine_parts[1])

    return sum(gear_ratios)


if __name__ == '__main__':  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
