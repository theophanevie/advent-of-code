import sys
from typing import TextIO, List, Tuple

def parseinput(inputfile: TextIO) -> Tuple[List[Tuple[int, int]], int]:
    start = int(inputfile.readline())
    
    line = inputfile.readline().strip().split(',')
    bus = []
    
    for i, busid in enumerate(line):
        if busid != 'x':
            bus.append((int(busid),i))

    bus.sort(key=lambda  x: x[0])

    return bus, start


def check_firstpart(filename: str) -> int:
    with open(filename,'r') as inputfile:
        bus, start = parseinput(inputfile)

    i = 0
    towait = 0

    while (start + towait) % bus[i][0] != 0:
        i += 1

        if i >= len(bus):
            i = 0
            towait += 1

    return towait * bus[i][0]

    
        
def check_secondpart(filename: str) -> int:
    with open(filename,'r') as inputfile:
       bus, start = parseinput(inputfile)
    
    nbbus = len(bus)
    start = 0
    
    offset = 1
    i = 0
    while i < len(bus):

        valid = False
        while not valid:

            start += offset
            # print(f'test number {start=}')
            valid = True
            for j in range(i + 1):
                if (start + bus[j][1]) % bus[j][0] != 0:
                    valid = False
                    break

        for j in range(i + 1):
            print(f'{start} + {bus[j][1]} % {bus[j][0]} , {(start + bus[j][1]) % bus[j][0] == 0}')

        offset *= bus[i][0]
        print("="*15)
        print(f'{start=}')
        print(f'{offset=}')
        print("="*15)
        i += 1

    return start
   


if __name__ == "__main__":
    print(check_secondpart(sys.argv[1]))
