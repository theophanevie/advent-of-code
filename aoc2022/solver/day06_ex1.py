import sys


def packet_start_pos(filename: str, header_len: int) -> int:
    datastream = open(filename, "r").read().strip()
    buffer = []

    for i, letter in enumerate(datastream):
        if len(buffer) < header_len:
            buffer.append(letter)
            continue

        buffer.pop(0)
        buffer.append(letter)

        if len(set(buffer)) == header_len:
            return i + 1

    assert False


if __name__ == "__main__":
    print(packet_start_pos(sys.argv[1], int(sys.argv[2])))
