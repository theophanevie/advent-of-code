import sys
from collections import defaultdict
from typing import TextIO

def bruteforce(inputfile: TextIO, totaltour: int) -> int:

    # tuple with n tour and n - 1 tour when number has been seen
    number = defaultdict(lambda: (0, 0))
    tour = 1

    # init game with starting numbers
    for nb in inputfile.readline().strip().split(','):
        number[int(nb)] = (tour, 0)
        tour += 1

    spoken = 0
    tour += 1

    # play game until wanted tour
    while tour <= totaltour:
        
        isnewnumber = spoken in number.keys()
        number[spoken] = (tour - 1, number[spoken][0])

        if isnewnumber:
            spoken = number[spoken][0] - number[spoken][1]

        else:
            spoken = 0

        tour += 1

    return spoken


def check_firstpart(filename: str) -> int:
    with open(filename,'r') as inputfile:
       return bruteforce(inputfile, 2020)
   

        
def check_secondpart(filename: str) -> int:
    with open(filename,'r') as inputfile:
       return bruteforce(inputfile, 30000000)


if __name__ == "__main__":
    print(f"firstpart {check_firstpart(sys.argv[1])}")
    print(f"seconfpart {check_secondpart(sys.argv[1])}")
