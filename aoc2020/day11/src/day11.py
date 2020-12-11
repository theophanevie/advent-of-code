import sys
from typing import TextIO, List
from copy import deepcopy


def countseat(seatmap: List[str]) -> int:
    cpt = 0
    for line in seatmap:
        cpt += line.count('#')
    return cpt


def itepart1(seatmap: List[str]) -> int:
    lseatmap = len(seatmap)
    lline = len(seatmap[0])
    ret = deepcopy(seatmap)

    def isoccupied(i: int, offsetx: int, j: int, offsety: int) -> int:
        nonlocal lseatmap
        nonlocal lline
        nonlocal seatmap

        if (i + offsetx >= 0 and i + offsetx < lseatmap) and \
            (j + offsety >= 0 and j + offsety < lline):
                return seatmap[i + offsetx][j + offsety] == '#'
        
        return 0

    for i in range(lseatmap):
        for j in range(lline):

            if seatmap[i][j] == '.':
                continue

            occupied = 0

            occupied += isoccupied(i, -1, j, -1)
            occupied += isoccupied(i, 0, j, -1)
            occupied += isoccupied(i, 1, j, -1)

            occupied += isoccupied(i, -1, j, 1)
            occupied += isoccupied(i, 0, j, 1)
            occupied += isoccupied(i, 1, j, 1)

            occupied += isoccupied(i, -1, j, 0)
            occupied += isoccupied(i, 1, j, 0)

            if seatmap[i][j] == 'L' and occupied == 0:
                ret[i][j] = '#'
            elif seatmap[i][j] == '#' and occupied >= 4:
                ret[i][j] = 'L'
    
    return ret


def check_firstpart(filename: str) -> int:
    with open(filename,'r') as inputfile:
        seatmap = [list(line.strip()) for line in inputfile]

    save = deepcopy(seatmap)
    seatmap = itepart1(save)
    while(seatmap != save):
        save = deepcopy(seatmap)
        seatmap = itepart1(save)

    return countseat(seatmap)


def itepart2(seatmap: List[str]) -> int:
    lseatmap = len(seatmap)
    lline = len(seatmap[0])
    ret = deepcopy(seatmap)

    def isoccupied(i: int, offsetx: int, j: int, offsety: int) -> int:
        nonlocal lseatmap
        nonlocal lline
        nonlocal seatmap

        while (i + offsetx >= 0 and i + offsetx < lseatmap) and \
            (j + offsety >= 0 and j + offsety < lline):

            if seatmap[i + offsetx][j + offsety] == '.':
                i += offsetx
                j += offsety
            else: 
                return seatmap[i + offsetx][j + offsety] == '#'

        return 0

    for i in range(lseatmap):
        for j in range(lline):

            if seatmap[i][j] == '.':
                continue

            occupied = 0

            occupied += isoccupied(i, -1, j, -1)
            occupied += isoccupied(i, 0, j, -1)
            occupied += isoccupied(i, 1, j, -1)

            occupied += isoccupied(i, -1, j, 1)
            occupied += isoccupied(i, 0, j, 1)
            occupied += isoccupied(i, 1, j, 1)

            occupied += isoccupied(i, -1, j, 0)
            occupied += isoccupied(i, 1, j, 0)

            if seatmap[i][j] == 'L' and occupied == 0:
                ret[i][j] = '#'
            elif seatmap[i][j] == '#' and occupied >= 5:
                ret[i][j] = 'L'
    
    return ret


def check_secondpart(filename: str) -> int:
    with open(filename,'r') as inputfile:
        seatmap = [list(line.strip()) for line in inputfile]

    save = deepcopy(seatmap)
    seatmap = itepart2(save)
    while(seatmap != save):
        save = deepcopy(seatmap)
        seatmap = itepart2(save)

    return countseat(seatmap)

if __name__ == "__main__":
    print(check_first&part(sys.argv[1]))
