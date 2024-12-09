import itertools
import sys

antenna_locations = {}
antinode_locations = set()
antinode_locations_resonated = set()
max_x = 0
max_y = 0


def evaluate_antinodes(antenna_1, antenna_2):
    multiplier = 1
    while True:
        antinode = (antenna_1[0] + multiplier * (antenna_2[0] - antenna_1[0]),
                    antenna_1[1] + multiplier * (antenna_2[1] - antenna_1[1])
                    )
        if antinode[0] >= 0 and antinode[0] <= max_y and antinode[1] >= 0 and antinode[1] <= max_x:
            if multiplier == 2:
                antinode_locations.add(antinode)
                antinode_locations_resonated.add(antinode)
            else:
                antinode_locations_resonated.add(antinode)
            multiplier += 1
        else:
            break


def main(filename):
    with open(filename) as input_f:
        for y, line in enumerate(input_f):
            for x, char in enumerate(line.strip()):
                if char != ".":
                    antenna_locations.setdefault(char, []).append((y, x))

    global max_x
    global max_y
    max_x = x
    max_y = y

    for char, locations in antenna_locations.items():
        if len(locations) <= 1:
            continue
        combinations = list(itertools.combinations(locations, 2))
        for antenna_1, antenna_2 in combinations:
            evaluate_antinodes(antenna_1, antenna_2)
            evaluate_antinodes(antenna_2, antenna_1)

    print(f"Antinodes: {len(antinode_locations)}")
    print(f"Antinodes resonated: {len(antinode_locations_resonated)}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print(f"Usage: {sys.argv[0]} <input.txt>")
        sys.exit(1)
