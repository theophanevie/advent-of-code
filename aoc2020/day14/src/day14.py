import sys
import math
import re
import copy
from typing import List
from collections import defaultdict

def check_firstpart(filename: str) -> int:
    with open(filename,'r') as inputfile:
        p = re.compile("mem\[([0-9]*)\] = ([0-9]*)")

        mem = defaultdict(lambda: ["0"] * 36)
        
        for line in inputfile:
            line = line.strip()

            if line[:4] == 'mask':
                mask = line[7:]

            else:
                res = p.search(line)
                rowpos = int(res.group(1))

                # '3' -> 3 -> 0b11 -> '11'
                nbasb = str(bin(int(res.group(2))))[2:] 
                
                # less important bit to most important bit
                for bitpos in range(35, -1, -1):
                
                    # offset in nbasb
                    i = bitpos - (35 - len(nbasb)) - 1

                    bit = '0'

                    if mask[bitpos] != 'X':
                        bit = mask[bitpos]
                    elif i >= 0:
                        bit = nbasb[i]

                    mem[rowpos][bitpos] = bit

        res = 0
        for value in mem.values():
            res += int(''.join(value), 2)

        return res

def getmerow(cur: List[str], mask: List[str]) -> List[int]:
    res = []

    for i in range(2 ** cur.count('X')):
        toto = copy.deepcopy(cur)
        tmp = str(bin(i))[2:]

        j = 0
        for x in range(len(cur)):
            if toto[x] == 'X':
                toto[x] = tmp[- j - 1] if j < len(tmp) else '0'
                j += 1
    
        res.append(int(''.join(toto), 2))

    return res

        
def check_secondpart(filename: str) -> int:
    with open(filename,'r') as inputfile:
        p = re.compile("mem\[([0-9]*)\] = ([0-9]*)")

        mem = defaultdict(lambda: ["0"] * 36)
        
        for line in inputfile:
            line = line.strip()

            if line[:4] == 'mask':
                mask = line[7:]

            else:
                res = p.search(line)
                rowpos = int(res.group(1))
                cur = ["0"] * 36

                # '3' -> 3 -> 0b11 -> '11'
                nbasb = str(bin(int(res.group(1))))[2:]

                # less important bit to most important bit
                for bitpos in range(35, -1, -1):
                
                    # offset in nbasb
                    i = bitpos - (35 - len(nbasb)) - 1

                    bit = '0'

                    if mask[bitpos] != '0':
                        bit = mask[bitpos]
                    elif i >= 0:
                        bit = nbasb[i]

                    cur[bitpos] = bit


                nbasb = str(bin(int(res.group(2))))[2:]
                nb = ["0"] * 36
                for bitpos in range(35, -1, -1):
                    bit = '0'
                    i = bitpos - (35 - len(nbasb)) - 1
                    if i >= 0:
                        bit = nbasb[i]

                    nb[bitpos] = bit


                for val in getmerow(cur, mask):
                    mem[val] = nb


        res = 0
        for value in mem.values():
            res += int(''.join(value), 2)

        return res


if __name__ == "__main__":
    print(check_secondpart(sys.argv[1]))
