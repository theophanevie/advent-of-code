import sys
from collections import defaultdict

def ishiny(rules, key) -> int:
    cpt = 0
    if key in rules:
        for bag in rules[key]:
            if bag == 'shiny gold':
                cpt += 1
            else:
                cpt += ishiny(rules, bag)
    return cpt

def count_shiniy(rules) -> int:
    cpt = 0
    for key in rules.keys():
        cpt += ishiny(rules, key) >= 1
    return cpt

def check_firstpart(inputfile: str) -> int:
    colorbag = defaultdict(lambda: [])
    with open(inputfile,'r') as inputfile:
        for line in inputfile:
            line = line.strip().split()
            for i in range(4, len(line), 4):
                colorbag[f'{line[0]} {line[1]}']\
                    .append(f'{line[i + 1]} {line[i + 2]}')
    return count_shiniy(colorbag)
        
def shinybag(rules, key):
    cpt = 1
    for bag in rules[key]:
        if bag[1] != 0:
            cpt += bag[1] * shinybag(rules, bag[0])
    return cpt


def check(inputfile: str) -> int:
    colorbag = defaultdict(lambda: [])
    with open(inputfile,'r') as inputfile:
        for line in inputfile:
            line = line.strip().split()
            for i in range(4, len(line), 4):
                colorbag[f'{line[0]} {line[1]}']\
                    .append((f'{line[i + 1]} {line[i + 2]}', int(line[i] if line[i] != 'no' else '0')))
    return shinybag(colorbag, 'shiny gold') - 1

if __name__ == "__main__":
    print(check(sys.argv[1]))
