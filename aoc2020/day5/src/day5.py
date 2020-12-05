import sys
import math

def parsebpass(bpass: str, start: int, end: int) -> int:
    res = 0
    for i in range(start, end + 1):
        res += 2 ** (end - i) if bpass[i] in 'BR' else 0
    return res 

def check_firstpart(inputfile: str) -> int:
    with open(inputfile,'r') as inputfile:
        maxid = 0
        for line in inputfile:
            maxid = max(maxid, parsebpass(line, 0, 6) * 8 + parsebpass(line, 7, 9))
    return maxid
        

def check(inputfile: str) -> int:
    with open(inputfile,'r') as inputfile:
        l = []
        for line in inputfile:
            l.append(parsebpass(line, 0, 6) * 8 + parsebpass(line, 7, 9))
        l.sort()
        for i in range(len(l) - 1):
            if l[i] + 1 != l[i + 1]:
                return (l[i + 1] + l[i]) // 2
    return -1
        

if __name__ == "__main__":
    print(check_firstpart(sys.argv[1]))
