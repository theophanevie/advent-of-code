import sys
from collections import defaultdict

def check_firstpart(inputfile: str) -> int:
    with open(inputfile,'r') as inputfile:
        yes = 0
        group = defaultdict(lambda: 0)
        for line in inputfile:
            line = line.strip()
            if line == '':
                yes += len(group)
                group = defaultdict(lambda: 0)
            else:
                for i in range(len(line)):
                    group[line[i]] += 1
        yes += len(group)
    return yes



def check(inputfile: str) -> int:
    with open(inputfile,'r') as inputfile:
        yes = 0
        group = defaultdict(lambda: 0)
        groupsize = 0
        for line in inputfile:
            line = line.strip()
            if line == '':
                for val in group.values():
                    yes += 1 if val == groupsize else 0
                groupsize = 0
                group = defaultdict(lambda: 0)
            else:
                groupsize+= 1
                for i in range(len(line)):
                    group[line[i]] += 1
        for val in group.values():
            yes += 1 if val == groupsize else 0
    return yes

if __name__ == "__main__":
    print(check(sys.argv[1]))
