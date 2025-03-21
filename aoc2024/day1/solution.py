from sys import argv	

right, left = [], []

with open(argv[1], "r") as f:
    for line in f.readlines():
        x = line.split()
        right.append(int(x[0]))
        left.append(int(x[1]))

right.sort()
left.sort()

print(f"Part 1: {sum([max(right[i], left[i]) - min(right[i], left[i]) for i in range(len(right))])}")
print(f"Part 2: {sum([right[i] * left.count(right[i]) for i in range(len(right))])}")
