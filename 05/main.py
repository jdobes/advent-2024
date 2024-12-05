import sys


def is_update_valid(update, rules, swap=False):
    changed = True
    while changed:
        changed = False
        for rule in rules:
            idx_second = None
            for idx in range(len(update)):
                if update[idx] == rule[1]:
                    idx_second = idx
                elif update[idx] == rule[0] and idx_second is not None:
                    if swap:
                        num = update[idx_second]
                        update[idx_second] = update[idx]
                        update[idx] = num
                        changed = True
                        break
                    else:
                        return False
    return True


def main(filename):
    rules = []
    total_sum = 0
    total_sum_incorrect = 0
    with open(filename) as input_f:
        for line in input_f:
            if "|" in line:
                rule = line.split("|")
                rules.append((int(rule[0]), int(rule[1])))
            elif "," in line:
                update = [int(num) for num in line.split(",")]
                if is_update_valid(update, rules, swap=False):
                    total_sum += update[int(len(update)/2)]
                elif is_update_valid(update, rules, swap=True):
                    total_sum_incorrect += update[int(len(update)/2)]

    print(f"Sum: {total_sum}")
    print(f"Sum of incorrect: {total_sum_incorrect}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print(f"Usage: {sys.argv[0]} <input.txt>")
        sys.exit(1)
