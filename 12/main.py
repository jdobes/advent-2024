import sys


def count_sides(region, perimeter):  # Count corners actually
    sides = 0
    region = set(region)
    perimeter = set(perimeter)
    for point in region:
        if (point[0] - 1, point[1]) in perimeter and (point[0], point[1] - 1) in perimeter:
            sides += 1
        if (point[0] - 1, point[1]) in perimeter and (point[0], point[1] + 1) in perimeter:
            sides += 1
        if (point[0] + 1, point[1]) in perimeter and (point[0], point[1] - 1) in perimeter:
            sides += 1
        if (point[0] + 1, point[1]) in perimeter and (point[0], point[1] + 1) in perimeter:
            sides += 1
        if (point[0] - 1, point[1] - 1) in perimeter and (point[0] - 1, point[1]) in region and (point[0], point[1] - 1) in region:
            sides += 1
        if (point[0] - 1, point[1] + 1) in perimeter and (point[0] - 1, point[1]) in region and (point[0], point[1] + 1) in region:
            sides += 1
        if (point[0] + 1, point[1] + 1) in perimeter and (point[0] + 1, point[1]) in region and (point[0], point[1] + 1) in region:
            sides += 1
        if (point[0] + 1, point[1] - 1) in perimeter and (point[0] + 1, point[1]) in region and (point[0], point[1] - 1) in region:
            sides += 1
    return sides


def measure_region(farm, y_idx, x_idx):
    char = farm[y_idx][x_idx]
    y_max = len(farm) - 1
    x_max = len(farm[0]) - 1

    queue = [(y_idx, x_idx)]
    seen = {(y_idx, x_idx)}
    perimeter_points = []
    region = []
    while queue:
        plant = queue.pop(0)
        farm[plant[0]][plant[1]] = "."
        region.append(plant)
        for new in [(plant[0] + 1, plant[1]), (plant[0] - 1, plant[1]), (plant[0], plant[1] + 1), (plant[0], plant[1] - 1)]:
            if new[0] >= 0 and new[1] >= 0 and new[0] <= y_max and new[1] <= x_max and farm[new[0]][new[1]] == char:
                if new not in seen:
                    queue.append(new)
                    seen.add(new)
            elif new not in region:
                perimeter_points.append(new)

    area = len(region)
    perimeter = len(perimeter_points)
    sides = count_sides(region, perimeter_points)
    return area * perimeter, area * sides


def find_regions(farm):
    total_price = 0
    total_price_sides = 0
    for y_idx in range(len(farm)):
        for x_idx in range(len(farm[y_idx])):
            if farm[y_idx][x_idx] != ".":
                price, price_sides = measure_region(farm, y_idx, x_idx)
                total_price += price
                total_price_sides += price_sides
    return total_price, total_price_sides


def main(filename):
    farm = []
    with open(filename) as input_f:
        for line in input_f:
            row = []
            for char in line.strip():
                row.append(char)
            farm.append(row)

    total_price, total_price_sides = find_regions(farm)
    print(f"Total price: {total_price}")
    print(f"Total price counting sides: {total_price_sides}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print(f"Usage: {sys.argv[0]} <input.txt>")
        sys.exit(1)
