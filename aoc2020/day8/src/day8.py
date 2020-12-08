import sys
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from typing import List, TextIO
import copy


class Instruction(Enum):
    acc = 1
    nop = 2
    jmp = 3


@dataclass
class Line:
    instr: str
    offset: int 
    executed: bool

    def __init__(self, instr: Instruction, offset: int=-1):
        self.instr = instr
        self.offset = offset
        self.executed = False


def parseNumber(line: List[str]) -> int:
    sign = 1 if line[1][0] == '+' else -1
    return sign * int(line[1][1:])


def parseInput(inputfile: TextIO) -> List[Line]:
    l = []
    for line in inputfile:
        line = line.strip().split()

        if not line or line == ['']:
            break

        if line[0] == Instruction.acc.name:
            l.append(Line(Instruction.acc, parseNumber(line)))
        
        elif line[0] == Instruction.jmp.name:
            l.append(Line(Instruction.jmp, parseNumber(line)))

        elif line[0] == Instruction.nop.name:
            l.append(Line(Instruction.nop, parseNumber(line)))

        else:
            raise Exception("Invalid instruction")
    
    return l


def execute(l: List[Line]) -> int:
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


def check_firstpart(inputfile: str) -> int:
    with open(inputfile,'r') as inputfile:
        l = parseInput(inputfile)
    return execute(l)[0]
    

def check(inputfile: str) -> int:
    with open(inputfile,'r') as inputfile:
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
    print(check(sys.argv[1]))
