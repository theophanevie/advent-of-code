import sys


POS = tuple[int, int]
PADDING = 1


def parse_input(input_file: str) -> tuple[dict[POS, str], dict[int, POS]]:
    input_file = open(input_file, "r")
    universe = {}
    galaxies = {}
    galaxy_index = 0

    for y, line in enumerate(input_file.readlines()):
        line = line.strip()
        for x, obs in enumerate(line):
            if obs == "#":
                galaxies[galaxy_index] = (x, y)
                universe[x, y] = galaxy_index
                galaxy_index += 1

            else:
                universe[x, y] = obs

    return universe, galaxies


def expend_galaxies(universe: dict[POS, str], galaxies: dict[int, POS]):
    """
    Duplicate col and rows without any galaxy
    """
    offset = 0
    expended_galaxies = {}

    # For every col
    for x in range(max(obs[0] for obs in universe) + 1):
        col = [index for index, g in galaxies.items() if g[0] == x]

        # Insert col in expended universe
        for index in col:
            expended_galaxies[index] = (galaxies[index][0] + offset, galaxies[index][1])

        # Insert col again (duplicate col if no galaxy)
        if len(col) == 0:
            offset += PADDING

    # Reset offset
    offset = 0

    # For every row
    for y in range(max(obs[1] for obs in universe) + 1):
        row = [index for index, g in galaxies.items() if g[1] == y]

        # Insert row in expended universe
        for index in row:
            expended_galaxies[index] = (expended_galaxies[index][0], galaxies[index][1] + offset)

        # Insert col again (duplicate col if no galaxy)
        if len(row) == 0:
            offset += PADDING

    return expended_galaxies


def dist_from_galaxies(galaxies: list[POS]) -> dict[tuple[POS, POS], int]:
    distance = {}
    for galaxy_a in galaxies:
        for galaxy_b in galaxies:
            if (galaxy_b, galaxy_a) in distance:
                continue

            if galaxy_b == galaxy_a:
                continue

            distance[galaxy_a, galaxy_b] = abs(galaxy_b[0] - galaxy_a[0]) + abs(galaxy_b[1] - galaxy_a[1])

    return distance


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/7#part1
    """

    universe, galaxies = parse_input(input_file)

    # expend the universe and get new galaxy pos
    galaxies = expend_galaxies(universe, galaxies)

    distance = dist_from_galaxies(list(galaxies.values()))

    return sum(distance.values())


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
