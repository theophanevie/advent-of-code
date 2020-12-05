import sys
import math

def getcolumn(bpass: str) -> int:
    lpos = 0
    rpos = 7
    for i in range(7, 9, 1):
        if bpass[i] == 'L':
            rpos -= round((rpos - lpos) / 2)
        else:
            lpos += round((rpos - lpos) / 2)

    if bpass[9] == 'L':
        return lpos
    return rpos


def getrow(bpass: str) -> int:
    lpos = 0
    upos = 127
    for i in range(6):
        if bpass[i] == 'F':
            upos -= round((upos - lpos) / 2)
        else:
            lpos += round((upos - lpos) / 2)

    if bpass[6] == 'F':
        return lpos
    return upos

def check_firstpart(inputfile: str) -> int:
    with open(inputfile,'r') as inputfile:
        maxid = 0
        for line in inputfile:
            maxid = max(maxid, getrow(line) * 8 + getcolumn(line))
    return maxid
        

def check(inputfile: str) -> int:
    with open(inputfile,'r') as inputfile:
        l = []
        for line in inputfile:
            l.append(getrow(line) * 8 + getcolumn(line))
        l.sort()
        for i in range(len(l) - 1):
            if l[i] + 1 != l[i + 1]:
                return (l[i + 1] + l[i]) // 2
    return -1
        

if __name__ == "__main__":
    print(check(sys.argv[1]))
