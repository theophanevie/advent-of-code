from sys import argv

# Thanks to https://www.redblobgames.com/grids/hexagons/
# offset depends on parity
direction = [{
    "e": (1, 0),
    "ne": (1, -1),
    "nw": (0, -1),
    "w": (-1, 0),
    "sw": (0, 1),
    "se": (1, 1),
}, {
    "e": (1, 0),
    "ne": (0, -1),
    "nw": (-1, -1),
    "w": (-1, 0),
    "sw": (-1, 1),
    "se": (0, 1),
}]


identifiers = []
with open(argv[1], "r") as f:
    for line in f.readlines():
        l = line.strip()
        identifier, i = [], 0
        while i < len(l):
            if l[i] in "ns":
                identifier.append(l[i:i + 2])
                i += 2

            elif l[i] in "ew":
                identifier.append(l[i:i + 1])
                i += 1

            else:
                assert False  # Sanity check

        identifiers.sort()
        identifiers.append(identifier)


black_tiles = set()
for identifier in identifiers:
    pos = 0, 0
    for d in identifier:
        parity = pos[1] & 1
        pos = pos[0] + direction[parity][d][0], pos[1] + direction[parity][d][1]

    if pos in black_tiles:
        black_tiles.remove(pos)
    else:
        black_tiles.add(pos)

print(f"Part 1: {len(black_tiles)}")

for i in range(100):
    new_black_tiles = set()
    for x in range(-80, 80):
        for y in range(-80, 80):
            black_tiles_count = 0
            for d in direction[y & 1].values():
                if (x + d[0], y + d[1]) in black_tiles:
                    black_tiles_count += 1

            if (x, y) in black_tiles and 1 <= black_tiles_count <= 2:
                new_black_tiles.add((x, y))
            elif (x, y) not in black_tiles and black_tiles_count == 2:
                new_black_tiles.add((x, y))

    black_tiles = new_black_tiles

print(f"Part 2: {len(black_tiles)}")
