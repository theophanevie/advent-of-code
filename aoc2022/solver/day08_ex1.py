import sys


def hidden_tree(filename: str) -> None:
    forest_map = [line.strip() for line in open(filename, "r").readlines()]



    forest = []
    for _ in range(len(forest_map)):
        cur = []
        for _ in range(len(forest_map[0])):
            cur.append(0)
        forest.append(cur)


    for i in range(len(forest_map)):
        cur_max = -1
        for j in range(len(forest_map[0])):
            if int(forest_map[i][j]) > cur_max:
                cur_max = int(forest_map[i][j])
            else:
                forest[i][j] += 1

    for i in range(len(forest_map)):
        cur_max = -1
        for j in range(len(forest_map[0]) - 1, -1, -1):
            if int(forest_map[i][j]) > cur_max:
                cur_max = int(forest_map[i][j])
            else:
                forest[i][j] += 1


    for i in range(len(forest_map[0])):
        cur_max = -1
        for j in range(len(forest_map)):
            if int(forest_map[j][i]) > cur_max:
                cur_max = int(forest_map[j][i])
            else:
                forest[j][i] += 1

    for i in range(len(forest_map)):
        cur_max = -1
        for j in range(len(forest_map[0]) - 1, -1, -1):
            if int(forest_map[j][i]) > cur_max:
                cur_max = int(forest_map[j][i])
            else:
                forest[j][i] += 1

    for line in forest:
        print(line)

    trees = 0
    for line in forest:
        for nb in line:
            if nb == 4:
                trees += 1

    return len(forest_map[0]) * len(forest_map[0]) - trees


if __name__ == "__main__":
    print(hidden_tree(sys.argv[1]))
