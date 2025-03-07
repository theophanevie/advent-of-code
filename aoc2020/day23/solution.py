from sys import argv


class LinkedListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"<( val:{self.value} next:{repr(self.next.value)} )>"

def parse_input(part1: bool) -> tuple[dict[int, LinkedListNode], LinkedListNode]:
    jump_table = {}
    prev_cup, first_cup = None, None
    with open(argv[1], "r") as f:

        cups = [int(x) for x in f.readline().strip()]
        if not part1:
            cups += [i for i in range(10, 1000001)]

        for cup in cups:
            jump_table[cup] = LinkedListNode(cup)
            if first_cup is None:
                first_cup = jump_table[cup]

            if prev_cup is not None:
                prev_cup.next = jump_table[cup]
            prev_cup = jump_table[cup]

        prev_cup.next = first_cup

    return jump_table, first_cup

def play(jump_table: dict[int, LinkedListNode], first_cup: LinkedListNode, moves: int) -> dict[int, LinkedListNode]:
    cur_cup_index = first_cup.value
    for _ in range(moves):
        selection = []
        cur_cup = jump_table[cur_cup_index]

        tmp_cup = cur_cup
        for _ in range(3):
            selection.append(tmp_cup.next)
            tmp_cup = tmp_cup.next
        cur_cup.next = tmp_cup.next

        dest_cup_index = cur_cup_index - 1 if cur_cup_index > 1 else len(jump_table)
        while jump_table[dest_cup_index] in selection:
            dest_cup_index = dest_cup_index - 1 if dest_cup_index > 1 else len(jump_table)

        prev_next = jump_table[dest_cup_index].next
        jump_table[dest_cup_index].next = selection[0]
        selection[-1].next = prev_next

        cur_cup_index = jump_table[cur_cup_index].next.value

    return jump_table


# Part 1
jump_table, first_cup = parse_input(part1=True)
jump_table = play(jump_table, first_cup, 100)
res = [jump_table[1]]
while len(res) < len(jump_table):
    tmp = res[-1].next
    res.append(tmp)

print(f"Part 1: {"".join(str(node.value) for node in res[1:])}")

# Part 2
jump_table, first_cup = parse_input(part1=False)
jump_table = play(jump_table, first_cup, 10000000)
print(f"Part 2: {jump_table[1].next.value * jump_table[1].next.next.value}")
