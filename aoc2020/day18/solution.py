from sys import argv

expressions = []

with open(argv[1], "r") as f:
    for line in f.readlines():
        expressions.append(line.replace("(", "( ").replace(")", " )").split())


def eval_expression(exp, sign):
    buffer = []

    while len(exp) > 0:
        token, exp = exp[0], exp[1:]

        if token == "(":
            exp = eval_expression(exp)

        elif token == ")":
            return buffer + exp

        elif token.isdigit() or token in ["*", "+"]:
            buffer.append(token)

        else:
            assert False

        if len(buffer) == 3:
            exp = [str(eval("".join(buffer)))] + exp
            buffer = []

    return buffer + exp


part1 = sum(int(eval_expression(expression)[0]) for expression in expressions)
print(part1)
