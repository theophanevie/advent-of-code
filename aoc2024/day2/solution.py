from sys import argv

levels = []
with open(argv[1], "r") as f:
    for line in f.readlines():
        levels.append(list(map(int, line.strip().split())))


def is_safe(l: list[int]) -> bool:
    increasing = l[0] < l[1]

    for i in range(len(l) - 1):
        if (l[i] <= l[i + 1] and not increasing) or (l[i] >= l[i + 1] and increasing):
            return False

        if not (1 <=  abs(l[i] - l[i + 1])  <= 3):
            return False

    return True

part1 = 0
for lvl in levels:
    if is_safe(lvl):
        part1 += 1

print(f"Part 1: {part1}")

part2 = 0
for lvl in levels:
    if is_safe(lvl):
        part2 += 1
        continue

    safe = False
    for j in range(len(lvl)):
        if is_safe(lvl[:j] + lvl[j + 1:]):
            part2 += 1
            break

print(f"Part 2: {part2}")
