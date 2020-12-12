import sys
from enum import Enum
import math

class Direction(Enum):
    E = 0
    N = 90
    W = 180
    S = 270


class Ship():
    
    def __init__(self, usewaypoint: bool=False, offset_x: int=1, offset_y: int=0):
        self.coord_x = 0
        self.coord_y = 0
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.usewaypoint = usewaypoint


    def rotate(self, instr: str) -> None:
        rotation = -1 if instr[0] == 'R' else 1
        offsetangle = math.radians(int(instr[1:]) * rotation)

        tmpx = self.offset_x * int(math.cos(offsetangle))\
            - self.offset_y * int(math.sin(offsetangle))
        tmpy = self.offset_x * int(math.sin(offsetangle)) \
            + self.offset_y * int(math.cos(offsetangle))

        self.offset_x, self.offset_y = tmpx, tmpy


    def moove(self, instr: str) -> None:
        angle = math.radians(Direction[instr[0]].value)

        tmpx = int(math.cos(angle) * int(instr[1:]))
        tmpy = int(math.sin(angle) * int(instr[1:]))

        if self.usewaypoint:
            self.offset_x += tmpx
            self.offset_y += tmpy
        else:
            self.coord_x += tmpx
            self.coord_y += tmpy


    def getinstruction(self, instr: str) -> None:

        if instr[0] in 'LR':
            self.rotate(instr)

        elif instr[0] in 'F':
            self.coord_x += self.offset_x * int(instr[1:])
            self.coord_y += self.offset_y * int(instr[1:])

        elif instr[0] in 'NESW':
            self.moove(instr)
            

def check_firstpart(filename: str) -> int:
    with open(filename,'r') as inputfile:
        instructions = [line.strip() for line in inputfile]

    ship = Ship()

    for instr in instructions:
        ship.getinstruction(instr)

    return abs(ship.coord_y) + abs(ship.coord_x)

def check_secondpart(filename: str) -> int:
    with open(filename,'r') as inputfile:
        instructions = [line.strip() for line in inputfile]

    ship = Ship(usewaypoint=True, offset_x=10, offset_y=1)

    for instr in instructions:
        ship.getinstruction(instr)

    return abs(ship.coord_y) + abs(ship.coord_x)

if __name__ == "__main__":
    print(check_secondpart(sys.argv[1]))
