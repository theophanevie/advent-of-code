import sys
from typing import List, TextIO, Tuple

def isvalid(preambule: List[int], nb: int) -> bool:
    begin = len(preambule) - 25
    for i in range(begin, len(preambule)):
        for j in range(i + 1, len(preambule)):

            if preambule[i] + preambule[j] == nb:
                return True

    return False

        
def xmas(inputfile: TextIO) -> Tuple[int, List[int]]:
    preambule : List[int] = []

    for line in inputfile:
        curnb = int(line.strip())

        if len(preambule) < 25:
            preambule.append(curnb)
        else:
            if not isvalid(preambule, curnb):
                return curnb, preambule
            preambule.append(curnb)
    
    return -1, []


def check_firstpart(filename: str) -> int:
    with open(filename,'r') as inputfile:
        return xmas(inputfile)[0]


def check_secondpart(filename: str) -> int:
    with open(filename,'r') as inputfile:
        invalidnb, preambule = xmas(inputfile)

    for i in range(len(preambule)):
        solution = [preambule[i]]

        for j in range(i + 1, len(preambule)):
            solution.append(preambule[j])

            if sum(solution) == invalidnb:
                return min(solution) + max(solution)

    return -1

if __name__ == "__main__":
    print(check_secondpart(sys.argv[1]))
