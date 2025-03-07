from sys import argv	
	
with open(argv[1], "r") as f:
    card_pkey = int(f.readline().strip())
    door_pkey = int(f.readline().strip())


def get_loop_size(pkey: int) -> int:
    i = 0
    subject_number = 7
    loop_size = 1
    while loop_size != pkey:
        loop_size *= subject_number
        loop_size = loop_size % 20201227
        i += 1

    return i

def get_key(loop_size: int, subject_number) -> int:
    tmp = 1
    for _ in range(loop_size):
        tmp *= subject_number
        tmp = tmp % 20201227
    return tmp

card_loop_size = get_loop_size(card_pkey)
door_loop_size = get_loop_size(door_pkey)

private_key = get_key(card_loop_size, door_pkey)
assert private_key == get_key(door_loop_size, card_pkey)

print(f"Part 1: {private_key}")
