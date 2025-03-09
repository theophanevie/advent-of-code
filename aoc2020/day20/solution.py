from enum import Enum
import math
from sys import argv
import re


# Disclaimer: Sorry about this code, it needs """"some""" refactoring.


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Tile:
    def __init__(self, tile_id: int, content: list[str]):
        self.tile_id = tile_id
        self.content = content

    def rotate(self) -> None:
        new_content = []
        for i in range(len(self.content)):
            new_content.append("".join([row[len(row) - i - 1] for row in self.content]))
        self.content = new_content

    def vertical_flip(self) -> None:
        self.content = [row[::-1] for row in self.content]

    def horizontal_flip(self) -> None:
        self.content.reverse()

    def match(self, d: Direction, t: "Tile") -> bool:
        match d:
            case Direction.UP:
                return self.content[0] == t.content[-1]
            case Direction.DOWN:
                return self.content[-1] == t.content[0]
            case Direction.LEFT:
                return "".join(row[0] for row in self.content) == "".join(row[-1] for row in t.content)
            case Direction.RIGHT:
                return "".join(row[0] for row in t.content) == "".join(row[-1] for row in self.content)

    def can_match(self, t: "Tile") -> bool:
        return len(set(self.edges).intersection(set(t.edges))) > 0

    def shrink(self) -> None:
        self.content = [row[1:-1] for row in self.content[1:-1]]

    @property
    def edges(self) -> list[str]:
        edges = [self.content[0], self.content[-1], "".join([l[0] for l in self.content]), "".join([l[-1] for l in self.content])]
        return edges + [e[::-1] for e in edges]

    def __repr__(self) -> str:
        return str(self.tile_id)

    def __eq__(self, other):
        return self.tile_id == other.tile_id

    def print(self) -> None:
        for row in self.content:
            print(row)

tiles = []
with open(argv[1], "r") as f:
    for image in f.read().split("\n\n"):
        tile_id = re.match(r"Tile (\d+)", image).group(1)
        if tile_id == "0":  # Hardcoded stop at the last tile
            break

        tiles.append(Tile(int(tile_id), [l.strip() for l in image.split("\n")][1:]))

grid_size = int(math.sqrt(len(tiles)))

def find_top_left(tiles: list[Tile]) -> Tile:
    for t1 in tiles:
        edge_match = 0
        for t2 in tiles:
            if t1 == t2:
                continue
            for e in t1.edges:
                if e in t2.edges:
                    edge_match += 1
        if edge_match == 4:
            found = False
            for tile in tiles:
                if match(Direction.DOWN, t1, tile):
                    found = True
                    break
            if not found:
                for _ in range(3):
                   t1.rotate()
            return t1


def match(d: Direction, t1: Tile, t2: Tile) -> bool:
    for _ in range(4):
        if t1.match(d, t2):
            return True
        t2.rotate()
    t2.vertical_flip()
    for _ in range(4):
        if t1.match(d, t2):
            return True
        t2.rotate()
    t2.vertical_flip()
    t2.horizontal_flip()
    for _ in range(4):
        if t1.match(d, t2):
            return True
        t2.rotate()
    return False

grid = {(0, 0): find_top_left(tiles)}
tiles.remove(grid[(0, 0)])

for i in range(1, grid_size):
    for tile in tiles:
        if match(Direction.DOWN, grid[(i - 1, 0)], tile):
            grid[(i, 0)] = tile
            break
    tiles.remove(grid[(i, 0)])

for i in range(0, grid_size):
    for j in range(1, grid_size):
        for tile in tiles:
            if match(Direction.RIGHT, grid[(i, j - 1)], tile):
                grid[(i, j)] = tile
                break
        tiles.remove(grid[(i, j)])

print(f"Part 1: {grid[(0,0)].tile_id * grid[(grid_size -1,0)].tile_id * grid[(0,grid_size - 1)].tile_id * grid[(grid_size - 1, grid_size - 1)].tile_id}")


for i in range(0, grid_size):
    for j in range(0, grid_size):
        grid[(i, j)].shrink()

img = []
for i in range(0, grid_size):
    for x in range(len(grid[(0, 0)].content)):
        img.append("".join([grid[(i, j)].content[x] for j in range(0, grid_size)]))

t = Tile(0, img)

def find_monster(tile: Tile) -> int:
    for _ in range(4):
        monster = 0
        for i in range(len(tile.content) - 2):
            for j in range(0, len(tile.content[0]) - 20):
                m1 = re.match(r"..................#.", tile.content[i][j:j + 20])
                m2 = re.match(r"#....##....##....###", tile.content[i + 1][j:j + 20])
                m3 = re.match(r".#..#..#..#..#..#...", tile.content[i + 2][j:j + 20])
                if m1 and m2 and m3:
                    monster += 1
        if monster > 0:
            return monster

        t.rotate()
    return 0

monster = find_monster(t)
if monster == 0:
    t.vertical_flip()
    monster = find_monster(t)
if monster == 0:
    t.vertical_flip()
    t.horizontal_flip()
    monster = find_monster(t)

assert monster != 0

part2 = sum([row.count("#") for row in t.content]) - monster * 15

print(f"Part 2: {part2}")
