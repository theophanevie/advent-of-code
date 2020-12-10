import sys
from typing import TextIO

def check_firstpart(filename: str) -> int:
    adpt = [0]
    
    with open(filename,'r') as inputfile:
        for line in inputfile:
            adpt.append(int(line.strip()))

    adpt.sort()

    diff1_nb = 0
    diff3_nb = 0
    for i in range(len(adpt) - 1):
        
        if adpt[i + 1] - adpt[i] == 1:
            diff1_nb += 1

        elif adpt[i + 1] - adpt[i] == 3:
            diff3_nb += 1

    return diff1_nb * (diff3_nb + 1)


def check_secondpart(filename: str) -> int:
    adpt = [0]
    
    with open(filename,'r') as inputfile:
        for line in inputfile:
            adpt.append(int(line.strip()))

    adpt.sort()

    ite = [0] * len(adpt)
    ite[0] = 1

    for i in range(len(adpt)):

        for j in range(i + 1, min(i + 4, len(adpt))):

            if adpt[j] - adpt[i] <= 3:
                ite[j] += ite[i]

    return ite[-1]

if __name__ == "__main__":
    print(check_secondpart(sys.argv[1]))
