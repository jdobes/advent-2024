import sys


def main(filename):
    left_col = []
    right_col = []

    with open(filename) as input_f:
        for line in input_f:
            cols = line.split()
            if len(cols) != 2:
                print(f"2 columns are expected, received: {cols}")
                sys.exit(2)
            left_col.append(int(cols[0]))
            right_col.append(int(cols[1]))

    left_col.sort()
    right_col.sort()

    total_distance = 0
    for idx in range(len(left_col)):
        total_distance += abs(left_col[idx] - right_col[idx])
    print(total_distance)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print(f"Usage: {sys.argv[0]} <input.txt>")
        sys.exit(1)
