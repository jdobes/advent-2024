import re
import sys


def main(filename):
    pattern = re.compile("(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)")
    total_sum = 0
    enabled_sum = 0
    enabled = True
    with open(filename) as input_f:
        for line in input_f:
            matches = pattern.findall(line)
            for match in matches:
                if match[0]:  # do()
                    enabled = True
                elif match[1]:  # don't()
                    enabled = False
                else:
                    single_sum = int(match[2]) * int(match[3])
                    total_sum += single_sum
                    if enabled:
                        enabled_sum += single_sum

    print(f"Total sum: {total_sum}")
    print(f"Enabled sum: {enabled_sum}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print(f"Usage: {sys.argv[0]} <input.txt>")
        sys.exit(1)
