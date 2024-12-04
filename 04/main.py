import sys


def check_c(matrix, x, y, c):
    return y >= 0 and y < len(matrix) and x >=0 and x < len(matrix[0]) and matrix[y][x] == c


def check_left(matrix, x, y):
    return (
        check_c(matrix, x, y, "X") and
        check_c(matrix, x - 1, y, "M") and
        check_c(matrix, x - 2, y, "A") and
        check_c(matrix, x - 3, y, "S")
    )


def check_right(matrix, x, y):
    return (
        check_c(matrix, x, y, "X") and
        check_c(matrix, x + 1, y, "M") and
        check_c(matrix, x + 2, y, "A") and
        check_c(matrix, x + 3, y, "S")
    )


def check_up(matrix, x, y):
    return (
        check_c(matrix, x, y, "X") and
        check_c(matrix, x, y + 1, "M") and
        check_c(matrix, x, y + 2, "A") and
        check_c(matrix, x, y + 3, "S")
    )


def check_down(matrix, x, y):
    return (
        check_c(matrix, x, y, "X") and
        check_c(matrix, x, y - 1, "M") and
        check_c(matrix, x, y - 2, "A") and
        check_c(matrix, x, y - 3, "S")
    )


def check_up_left(matrix, x, y):
    return (
        check_c(matrix, x, y, "X") and
        check_c(matrix, x - 1, y + 1, "M") and
        check_c(matrix, x - 2, y + 2, "A") and
        check_c(matrix, x - 3, y + 3, "S")
    )


def check_up_right(matrix, x, y):
    return (
        check_c(matrix, x, y, "X") and
        check_c(matrix, x + 1, y + 1, "M") and
        check_c(matrix, x + 2, y + 2, "A") and
        check_c(matrix, x + 3, y + 3, "S")
    )


def check_down_left(matrix, x, y):
    return (
        check_c(matrix, x, y, "X") and
        check_c(matrix, x - 1, y - 1, "M") and
        check_c(matrix, x - 2, y - 2, "A") and
        check_c(matrix, x - 3, y - 3, "S")
    )


def check_down_right(matrix, x, y):
    return (
        check_c(matrix, x, y, "X") and
        check_c(matrix, x + 1, y - 1, "M") and
        check_c(matrix, x + 2, y - 2, "A") and
        check_c(matrix, x + 3, y - 3, "S")
    )


def check_x(matrix, x, y):
    return (
        check_c(matrix, x, y, "A") and (
            (
                # M.S
                # .A.
                # M.S
                check_c(matrix, x - 1, y + 1, "M") and
                check_c(matrix, x - 1, y - 1, "M") and
                check_c(matrix, x + 1, y + 1, "S") and
                check_c(matrix, x + 1, y - 1, "S")
            ) or (
                # S.M
                # .A.
                # S.M
                check_c(matrix, x - 1, y + 1, "S") and
                check_c(matrix, x - 1, y - 1, "S") and
                check_c(matrix, x + 1, y + 1, "M") and
                check_c(matrix, x + 1, y - 1, "M")
            ) or (
                # M.M
                # .A.
                # S.S
                check_c(matrix, x - 1, y + 1, "M") and
                check_c(matrix, x - 1, y - 1, "S") and
                check_c(matrix, x + 1, y + 1, "M") and
                check_c(matrix, x + 1, y - 1, "S")
            ) or (
                # S.S
                # .A.
                # M.M
                check_c(matrix, x - 1, y + 1, "S") and
                check_c(matrix, x - 1, y - 1, "M") and
                check_c(matrix, x + 1, y + 1, "S") and
                check_c(matrix, x + 1, y - 1, "M")
            )
        )
    )


def main(filename):
    matrix = []
    with open(filename) as input_f:
        for line in input_f:
            matrix.append(line)

    counter = 0
    counter_x = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if check_left(matrix, col, row):
                counter += 1
            if check_right(matrix, col, row):
                counter += 1
            if check_up(matrix, col, row):
                counter += 1
            if check_down(matrix, col, row):
                counter += 1
            if check_up_left(matrix, col, row):
                counter += 1
            if check_up_right(matrix, col, row):
                counter += 1
            if check_down_left(matrix, col, row):
                counter += 1
            if check_down_right(matrix, col, row):
                counter += 1
            if check_x(matrix, col, row):
                counter_x += 1

    print(f"Count XMAS: {counter}")
    print(f"Count X-MAS: {counter_x}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print(f"Usage: {sys.argv[0]} <input.txt>")
        sys.exit(1)
