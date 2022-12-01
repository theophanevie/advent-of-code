import sys

def compute_max_cal(filename: str) -> int:
    max_cal = []
    cur_cal = 0

    list_snack = open(filename, 'r').readlines()
    list_snack.append('')

    for snack in list_snack:
        snack = snack.strip()

        if snack == '':

            if len(max_cal) < 3:
                max_cal.append(cur_cal)

            elif cur_cal > max_cal[0]:

                max_cal.append(cur_cal)
                max_cal.sort()
                max_cal = max_cal[1:]

            cur_cal = 0
            continue

        cur_cal += int(snack)

    return sum(max_cal)

if __name__ == "__main__":
    print(compute_max_cal(sys.argv[1]))
