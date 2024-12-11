import sys


def blink(stones):
    new_stones = {}
    for stone in stones:
        len_stone = len(str(stone))
        if stone == 0:
            if 1 not in new_stones:
                new_stones[1] = 0
            new_stones[1] += stones[0]
        elif len_stone % 2 == 0:
            left_part = int(str(stone)[0:int(len_stone / 2)])
            right_part = int(str(stone)[int(len_stone / 2):])
            if left_part not in new_stones:
                new_stones[left_part] = 0
            new_stones[left_part] += stones[stone]
            if right_part not in new_stones:
                new_stones[right_part] = 0
            new_stones[right_part] += + stones[stone]
        else:
            if (stone * 2024) not in new_stones:
                new_stones[stone * 2024] = 0
            new_stones[stone * 2024] += stones[stone]
    return new_stones


def main(filename):
    stones = {}
    with open(filename) as input_f:
        for line in input_f:
            for num in line.split():
                num = int(num)
                if num not in stones:
                    stones[num] = 1
                else:
                    stones[num] += 1

    for _ in range(25):
        stones = blink(stones)

    print(f"Stones after 25 blinks: {sum(stones.values())}")

    for _ in range(50):
        stones = blink(stones)

    print(f"Stones after 75 blinks: {sum(stones.values())}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print(f"Usage: {sys.argv[0]} <input.txt>")
        sys.exit(1)
