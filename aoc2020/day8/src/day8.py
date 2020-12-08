import sys
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from typing import List, TextIO, Tuple
import copy


class Instruction(Enum):
    acc = 1
    nop = 2
    jmp = 3


@dataclass
class Line:
    instr: Instruction
    offset: int 
    executed: bool = False

    def __init__(self, instr: Instruction, offset: int):
        self.instr = instr
        self.offset = offset


def parseInput(inputfile: TextIO) -> List[Line]:
    l = []
    for curline in inputfile:
        line = curline.strip().split()

        if not line or line == ['']:
            break

        if line[0] == Instruction.acc.name:
            l.append(Line(Instruction.acc, int(line[1])))
        
        elif line[0] == Instruction.jmp.name:
            l.append(Line(Instruction.jmp, int(line[1])))

        elif line[0] == Instruction.nop.name:
            l.append(Line(Instruction.nop, int(line[1])))

        else:
            raise Exception("Invalid instruction")
    
    return l


def execute(l: List[Line]) -> Tuple[int, int]:
    acc = 0
    i = 0
    while i != len(l) and not l[i].executed:

        curline = l[i]
        curline.executed = True

        if curline.instr == Instruction.acc:
            acc += curline.offset

        if curline.instr == Instruction.jmp:
            i += curline.offset
        else:
            i += 1

    return acc, i


def check_firstpart(filename: str) -> int:
    with open(filename,'r') as inputfile:
        l = parseInput(inputfile)
    return execute(l)[0]
    

def check_secondpart(filename: str) -> int:
    with open(filename,'r') as inputfile:
        li = parseInput(inputfile)

    j = 0
    i = 0
    while i != len(li):
        
        l = copy.deepcopy(li)

        #search for next nop/jmp not yet modified
        curupdate = l[j]
        while curupdate.instr != Instruction.nop and \
                curupdate.instr != Instruction.jmp:
            j += 1
            curupdate = l[j]

        if curupdate.instr == Instruction.nop:
            curupdate.instr = Instruction.jmp
        else:
            curupdate.instr = Instruction.nop

        acc, i = execute(l)

        j+= 1

    return acc

if __name__ == "__main__":
    print(check_secondpart(sys.argv[1]))
