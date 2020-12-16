import sys
import re
from typing import TextIO, Dict, List, Tuple, DefaultDict
import copy
import random
from collections import defaultdict

def getregex(inputfile: TextIO) -> Dict[str, List[int]]:
    """
    Create a dict with all regex : 
    - key : ticket field name
    - value : list of all possible value for this field
    """
    line = inputfile.readline().strip()
    field = {}

    while line != '':
        pos1 = line.find(':')
        pos2 = line.find('or', pos1 + 1)
        pos3 = line.find('-')
        pos4 = line.find('-', pos3 + 1)

        fieldname = line[:pos1]

        value = [i for i in range(int(line[pos1 + 2:pos3]), \
            int(line[pos3 + 1:pos2 - 1]) + 1)]
        value += [i for i in range(int(line[pos2 +3:pos4]), \
            int(line[pos4 + 1:]) + 1)]

        field[fieldname] = value

        line = inputfile.readline().strip()

    return field


def suminvalidfield(line: List[str], field: Dict) -> int:
    """
    Sum all invalid value for all fields in current ticket (line)
    """
    res = 0
    for i in range(len(line)):
        nb = int(line[i])

        valid = False
        for fieldvalue in field.keys():
            
            if nb in field[fieldvalue]:
                valid = True
                break

        if not valid:
            res += nb
    
    return res


def check_firstpart(filename: str) -> int:
    with open(filename,'r') as inputfile:
        field = getregex(inputfile)

        line = inputfile.readline().strip()
        while line != 'nearby tickets:':
            line = inputfile.readline().strip()

        res = 0
        for line in inputfile:
            res += suminvalidfield(line.strip().split(','), field)

        return res


def fieldposition(line: List[str], field: Dict[str, List[int]]) \
        -> DefaultDict[str, List[int]]:
    """
    Create a dict with all valid position for a field
    """
    fieldpos = defaultdict(lambda: [])

    for i in range(len(line)):
        nb = int(line[i])

        for fieldvalue in field.keys():
            
            if nb in field[fieldvalue]:
                fieldpos[fieldvalue].append(i)
    
    return fieldpos

def mergeset(curticket: Dict[str, List[int]], ticket: Dict[str, List[int]]) -> None:
    """
    if curent ticket is valid, select a field and remove all occurence of the position of this field in ticket
    """
    s = set()
    for key in curticket.keys():
        for val in curticket[key]:
            s.add(val)

    if len(s) != len(ticket.keys()):
        return

    for key in ticket.keys():
        ticket[key] =  list(set(ticket[key]).intersection(curticket[key]))

def matchfield(ticket: Dict[str, List[int]], ticketvalue: List[str]) -> int:
    """
    valide a field if only one position is possible for it
    multiply value from ticket where validate field contains departure
    """
    res = 1
    departurefield = 0

    while departurefield < 6:
        for key in ticket.keys():

            if len(ticket[key]) == 1:
                nb = ticket[key][0]

                if re.match("departure", key):
                    res *= int(ticketvalue[nb])
                    departurefield += 1
                break
        
        del ticket[key]
        
        for key in ticket.keys():
            if nb in ticket[key]:
                ticket[key].remove(nb)

    return res

def check_secondpart(filename: str) -> int:
    with open(filename,'r') as inputfile:
        field = getregex(inputfile)

        line = inputfile.readline().strip()
        while line != 'your ticket:':
            line = inputfile.readline().strip()
        
        ticketvalue = inputfile.readline().strip().split(',')
        ticket = fieldposition(ticketvalue, field)

        while line != 'nearby tickets:':
            line = inputfile.readline().strip()

        line = inputfile.readline().strip()

        for line in inputfile:
            curticket = fieldposition(line.strip().split(','), field)
            mergeset(curticket, ticket)

    return matchfield(ticket, ticketvalue)



if __name__ == "__main__":
    print(f"firstpart {check_firstpart(sys.argv[1])}")
    print(f"secondpart {check_secondpart(sys.argv[1])}")
