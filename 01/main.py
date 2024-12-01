import sys


def main(filename):
    left_col = []
    right_col = []
    right_col_appearances = {}

    with open(filename) as input_f:
        for line in input_f:
            cols = line.split()
            if len(cols) != 2:
                print(f"2 columns are expected, received: {cols}")
                sys.exit(2)
            left_col.append(int(cols[0]))
            right_num = int(cols[1])
            right_col.append(right_num)
            if right_num not in right_col_appearances:
                right_col_appearances[right_num] = 0
            right_col_appearances[right_num] += 1

    left_col.sort()
    right_col.sort()

    total_distance = 0
    total_similarity = 0
    for idx in range(len(left_col)):
        total_distance += abs(left_col[idx] - right_col[idx])
        total_similarity += left_col[idx] * right_col_appearances.get(left_col[idx], 0)
    print(f"Part one: {total_distance}")
    print(f"Part two: {total_similarity}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print(f"Usage: {sys.argv[0]} <input.txt>")
        sys.exit(1)
