import sys


def load_file(filename: str) -> tuple[list[list[str]], list[list[str]]]:
    # This is ugly :/
    file_tmp = open(filename, "r").readlines()
    file_content = [line.strip() for line in file_tmp]
    middle_of_file = file_content.index("")

    instructions = [instruction.split(" ") for instruction in file_content[middle_of_file + 1:]]

    stacks = []
    for x in range(0, len(file_tmp[middle_of_file - 1]), 4):
        tmp_stack = []
        for line in file_tmp[:middle_of_file - 1]:

            if len(line) > x + 3:
                tmp_stack.append(line[x: x + 3])

        tmp_stack.reverse()
        stacks.append([x for x in tmp_stack if x != "   "])

    return stacks, instructions


def compute_new_stacks(filename: str, crane_9001: bool = False) -> str:
    stacks, instructions = load_file(filename)

    for instruction in instructions:
        buffer = []

        for _ in range(int(instruction[1])):
            buffer.append(stacks[int(instruction[3]) - 1].pop())

        if crane_9001:
            buffer.reverse()

        for x in buffer:
            stacks[int(instruction[5]) - 1].append(x)

    return "".join([stack[-1] for stack in stacks]).replace("]", "").replace("[", "")


if __name__ == "__main__":
    print(compute_new_stacks(sys.argv[1]))
