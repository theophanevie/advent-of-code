from sys import argv
from collections import deque

expressions = []

# Thanks to https://en.wikipedia.org/wiki/Shunting_yard_algorithm

with open(argv[1], "r") as f:
    for line in f.readlines():
        expressions.append(line.replace("(", "( ").replace(")", " )").split())

def shunt(tokens: deque) -> deque:
    operator = deque()
    output = deque()

    while len(tokens) > 0:
        token = tokens.popleft()

        if token.isdigit():
            output.append(token)

        elif token in operators.keys():

            while len(operator) > 0 and operator[-1] in operators.keys() and operators[operator[-1]] >= operators[token]:
                output.append(operator.pop())

            operator.append(token)

        elif token == "(":
            operator.append(token)

        elif token == ")":
            assert len(operator) > 0

            while operator[-1] != "(":
                output.append(operator.pop())

            assert operator[-1] == "("
            operator.pop()

        else:
            assert False  # Sanity check

    while len(operator) > 0:
        assert operator[-1] != "("
        output.append(operator.pop())

    return output

def eval_shunt(tokens: deque) -> int:
    buffer = []
    while len(tokens) > 0:
        token = tokens.popleft()

        if token.isdigit():
            buffer.append(token)

        elif token in operators.keys():
            assert len(buffer) >= 2
            buffer = buffer[:-2] + [eval(f"{buffer[-2]}{token}{buffer[-1]}")]

        else:
            assert False  # Sanity check

    assert len(buffer) == 1
    return buffer[0]


# All operators are left-associative
operators = {
    "+": 1,
    "*": 1,
}

part1 = sum([eval_shunt(shunt(deque(exp))) for exp in expressions])
print(f"Part 1: {part1}")

# All operators are left-associative
operators = {
    "+": 1,
    "*": 0,
}

part2 = sum([eval_shunt(shunt(deque(exp))) for exp in expressions])
print(f"Part 2: {part2}")
