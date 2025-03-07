from sys import argv

active = set()
with open(argv[1], "r") as f:
    for i, l in enumerate(f.readlines()):
        for c, ch in enumerate(l.strip()):
            if ch == "#":
                active.add((i, c, 0))

for _ in range(6):
    new_active = set()
    for y in range(-15, 15):
        for x in range(-15, 15):
            for z in range(-7, 7):
                active_neighbors = 0
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        for dz in [-1, 0, 1]:
                            pos = y + dy, x + dx, z + dz
                            if pos in active and (dy != 0 or dx != 0 or dz != 0):
                                active_neighbors += 1

                if (y, x, z) in active and active_neighbors in [2, 3]:
                    new_active.add((y, x, z))
                elif (y, x, z) not in active and active_neighbors == 3:
                    new_active.add((y, x, z))


    active = new_active

print(f"Part 1: {len(active)}")

active = set()
with open(argv[1], "r") as f:
    for i, l in enumerate(f.readlines()):
        for c, ch in enumerate(l.strip()):
            if ch == "#":
                active.add((i, c, 0, 0))

for _ in range(6):
    new_active = set()
    for y in range(-15, 15):
        for x in range(-15, 15):
            for z in range(-7, 7):
                for w in range(-7, 7):
                    active_neighbors = 0
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            for dz in [-1, 0, 1]:
                                for dw in [-1, 0, 1]:
                                    pos = y + dy, x + dx, z + dz, w + dw
                                    if pos in active and (dy != 0 or dx != 0 or dz != 0 or dw != 0):
                                        active_neighbors += 1

                    if (y, x, z, w) in active and active_neighbors in [2, 3]:
                        new_active.add((y, x, z, w))
                    elif (y, x, z, w) not in active and active_neighbors == 3:
                        new_active.add((y, x, z, w))


    active = new_active
print(f"Part 2: {len(active)}")
