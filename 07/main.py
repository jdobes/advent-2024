import itertools
import sys


def generate_operator_lists(count, with_concat=False):
    operators = ["+", "*"]
    if with_concat:
        operators.append("||")
    return list(itertools.product(operators, repeat=count))


def evaluate(operators, numbers):
    result = numbers[0]
    for idx, num in enumerate(numbers[1:]):
        if operators[idx] == "+":
            result += num
        elif operators[idx] == "*":
            result *= num
        elif operators[idx] == "||":
            result = int(str(result) + str(num))
    return result


def is_valid(test_value, numbers, with_concat=False):
    operator_lists = generate_operator_lists(len(numbers) - 1, with_concat=with_concat)
    for operators in operator_lists:
        if evaluate(operators, numbers) == test_value:
            return True
    return False


def main(filename):
    total_calibration_result = 0
    total_calibration_result_with_concat = 0
    with open(filename) as input_f:
        for line in input_f:
            parts = line.split(":")
            test_value = int(parts[0])
            numbers = [int(num) for num in parts[1].split()]
            if is_valid(test_value, numbers, with_concat=False):
                total_calibration_result += test_value
                total_calibration_result_with_concat += test_value
            elif is_valid(test_value, numbers, with_concat=True):
                total_calibration_result_with_concat += test_value

    print(f"Total calibration result: {total_calibration_result}")
    print(f"Total calibration result with concat: {total_calibration_result_with_concat}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print(f"Usage: {sys.argv[0]} <input.txt>")
        sys.exit(1)
