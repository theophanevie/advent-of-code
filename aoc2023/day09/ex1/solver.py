import sys


def parse_input(input_file: str) -> list[list[int]]:
    input_file = open(input_file, "r")

    sensor_reads = []

    for line in input_file.readlines():
        line = line.strip().split()
        sensor_reads.append([int(number) for number in line])

    return sensor_reads


def compute_pyramid(sensor_read: list[int]) -> list[list[int]]:
    pyramid = [sensor_read]

    while pyramid[-1].count(0) != len(pyramid[-1]):
        diff = []
        for i in range(len(pyramid[-1]) - 1):
            diff.append(pyramid[-1][i + 1] - pyramid[-1][i])
        pyramid.append(diff)

    return pyramid


def compute_next(pyramid: list[list[int]]) -> int:
    pyramid.reverse()

    offset = 0
    for stage in pyramid:
        stage.append(stage[-1] + offset)
        offset = stage[-1]

    return stage[-1]


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/7#part1
    """
    sensor_reads = parse_input(input_file)

    return sum(map(compute_next, map(compute_pyramid, sensor_reads)))


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
