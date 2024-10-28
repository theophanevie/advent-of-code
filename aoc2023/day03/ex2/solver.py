import sys
from collections import defaultdict

GEAR_SYMBOL = "*"


def reader(input_file: str) -> [str]:
    input_file = open(input_file, "r").readlines()

    return [line.strip() for line in input_file]


def find_gears(schematic: [str], y: int, x: int) -> [(int, int)]:
    """
    Check is there is a gear '*' adjacent to a given  x, y

    [ (y - 1, x - 1), (y - 1, x), (y - 1, x + 1) ]
    [ (y,     x - 1), (y,     x), (y,     x + 1) ]
    [ (y + 1, x - 1), (y + 1, x), (y + 1, x + 1) ]
    """
    gear_coordinates = []

    def test_x_axis(b: int, a: int):
        if a > 0:
            if GEAR_SYMBOL == schematic[b][a - 1]:
                gear_coordinates.append((b, a - 1))

        if GEAR_SYMBOL == schematic[b][a]:
            gear_coordinates.append((b, a))

        if a < len(schematic[0]) - 1:
            if GEAR_SYMBOL == schematic[b][a + 1]:
                gear_coordinates.append((b, a + 1))

        return None

    if y > 0:
        test_x_axis(y - 1, x)

    test_x_axis(y, x)

    if y < len(schematic) - 1:
        test_x_axis(y + 1, x)

    return gear_coordinates


def get_gears_engine_parts(schematic: [str]) -> dict[(int, int), [int]]:
    """
    Build a dictionary of :
        index: the gear coordinates
        values: a list of all engines part touching the gear
    """
    gears = defaultdict(list)

    for y in range(len(schematic)):
        number_buffer = ""
        # Set of gear coordinates affecting the motor part
        found_gears = set()

        for x in range(len(schematic[y])):
            # If the current character is a digit, it is added to the buffer, and we search for gear nearby
            if schematic[y][x].isdigit():
                number_buffer += schematic[y][x]
                found_gears |= set(find_gears(schematic, y, x))

            # If the current character is not a digit but the buffer is full, flush it
            elif len(number_buffer):
                number = int(number_buffer)
                for gear_coord in found_gears:
                    gears[gear_coord].append(number)

                found_gears = set()
                number_buffer = ""

        # Flush the buffer (only occurs if a digit was the last character of a line)
        if len(number_buffer):
            number = int(number_buffer)
            for gear_coord in found_gears:
                gears[gear_coord].append(number)

    return gears


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/3#part1
    """
    schematic = reader(input_file)
    gears = get_gears_engine_parts(schematic)

    # Construct a list of gear ratios for all gears that affect only two parts of the motor.
    gear_ratios = []
    for engine_parts in gears.values():
        if len(engine_parts) == 2:
            gear_ratios.append(engine_parts[0] * engine_parts[1])

    return sum(gear_ratios)


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
