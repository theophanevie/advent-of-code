import sys

def compute_view(x, y, forest_map, forest) -> list[int]:

    tree = int(forest_map[x][y])
    forest[x][y] = tree
    view = []

    tmp = 0
    for i in range(0, y):
        forest[x][i] = forest_map[x][i]
        tmp += 1
        if int(forest_map[x][i]) >= tree:
            break
    view.append(tmp)

    tmp = 0
    for i in range(y + 1, len(forest_map)):
        forest[x][i] = forest_map[x][i]
        tmp += 1
        if int(forest_map[x][i]) >= tree:
            break
    view.append(tmp)

    tmp = 0
    for i in range(0, x):
        forest[i][y] = forest_map[i][y]
        tmp += 1
        if int(forest_map[i][y]) >= tree:
            break
    view.append(tmp)

    tmp = 0
    for i in range(x + 1, len(forest_map)):
        forest[i][y] = forest_map[i][y]
        tmp += 1
        if int(forest_map[i][y]) >= tree:
            break
    view.append(tmp)

    print(f"{x} {y} {view}")

    toto = 1
    for i in view:
        toto *= i

    print(toto)
    return toto


def hidden_tree(filename: str) -> None:
    forest_map = [line.strip() for line in open(filename, "r").readlines()]


    for line in forest_map:
        print(line)
    forest = []
    for _ in range(len(forest_map)):
        cur = []
        for _ in range(len(forest_map[0])):
            cur.append(0)
        forest.append(cur)

    # for x in range(len(forest_map)):
    #     for y in range(len(forest_map[0])):

    compute_view(1, 2, forest_map, forest)






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
