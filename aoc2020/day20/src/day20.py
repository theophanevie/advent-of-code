import sys
from typing import List, TextIO
from dataclasses import dataclass
from copy import deepcopy
import re
import math

@dataclass
class Tile:
    """
    pos 0: up edge
    pos 1: right edge
    pos 2: down edge
    pos 3: left edge
    """
    lines : List[str]
    tile_id : int

    def __init__(self, lines: List[str], tile_id: int):
        self.lines = lines
        self.tile_id = tile_id


    def rotate(self, left: bool=True) -> None:
        if left:
            self.lines = list(zip(*self.lines))[::-1]
        else:
            for _ in range(3):
                self.lines = list(zip(*self.lines))[::-1]


    def flip(self, vertical: bool=True) -> None:
        if vertical:
            self.lines = list(zip(*self.lines[::-1]))
        else:
            self.lines = [tmp[::-1] for tmp in self.lines]

    def print(self) -> None:
        print('=' * 80)
        print(f'TILE {self.tile_id}')
        for line in self.lines:
            print(line)
        print('=' * 20)

def buildTiles(inputfile: TextIO) -> List[Tile]:
    tiles = []
    tile_id_regex = re.compile('Tile (.*):')

    for line in inputfile:

        tile_id = tile_id_regex.match(line.strip()).group(1)
        tmp = []

        for line in inputfile:

            line = line.strip()
            if line == '':
                break

            tmp.append(line)

        tiles.append(Tile(tmp, tile_id))

    return tiles

def buidlImg(tiles: List[str], img: List[List[int]]]) -> List[List[int]]]:
    return img

def check_firstpart(filename: str) -> int:
    with open(filename,'r') as inputfile:
        tiles = buildTiles(inputfile)

    img = [[-1] * int(math.sqrt(len(tiles)))] * int(math.sqrt(len(tiles)))

    img = buidlImg(tiles, img)

    return 0

def check_secondpart(filename: str) -> int:
    return check_firstpart(filename)

if __name__ == "__main__":
    print(f"firstpart {check_firstpart(sys.argv[1])}")
    print(f"secondpart {check_secondpart(sys.argv[1])}")
