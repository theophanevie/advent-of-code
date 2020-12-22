import sys
from typing import List, TextIO, Tuple, Set
from copy import deepcopy
    
def builddeck(inputfile: TextIO) -> Tuple[List[int], List[int]]:
    deck1, deck2 = [], []
    inputfile.readline()
    swap = False

    for line in inputfile:
        line = line.strip()

        if line == '':
            inputfile.readline()
            swap = True
            continue

        if swap:
            deck2.append(int(line))
        else:
            deck1.append(int(line))

    return deck1, deck2

def score(deck: List[int]) -> int:
    res = 0
    l = len(deck)

    for i in range(l):
        res += deck[i] * (l - i)

    return res
        
def playgame(deck1: List[int], deck2: List[int], subgame: bool=False) -> int:
    seen1, seen2 = [], []

    while len(deck1) > 0 and len(deck2) > 0:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if card1 <= len(deck1) and card2 <=len(deck2) and subgame:
            winner = playgame(deepcopy(deck1[:card1]), deepcopy(deck2[:card2]), subgame)
        else:
            winner = 1 if card1 > card2 else 2

        if winner == 1:
            deck1 += [card1, card2]
        else:
            deck2 += [card2, card1]
    

        if deck1 in seen1 and deck2 in seen2: 
            return 1

        else:
            seen1.append(deepcopy(deck1))
            seen2.append(deepcopy(deck2))



    if len(deck1) == 0:
        return 2
    return 1

def check_firstpart(filename: str) -> int:
    with open(filename,'r') as inputfile:
        deck1, deck2 = builddeck(inputfile)

    if playgame(deck1, deck2) == 1:
        return score(deck1)
    return score(deck2)

def check_secondpart(filename: str) -> int:
    with open(filename,'r') as inputfile:
        deck1, deck2 = builddeck(inputfile)

    if playgame(deck1, deck2, True) == 1:
        return score(deck1)
    return score(deck2)

if __name__ == "__main__":
    print(f"firstpart {check_firstpart(sys.argv[1])}")
    print(f"secondpart {check_secondpart(sys.argv[1])}")
