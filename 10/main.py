import sys


def in_bounds(place, topographic_map):
    return place[0] >= 0 and place[1] >=0 and place[0] < len(topographic_map) and place[1] < len(topographic_map[0])


def get_score(topographic_map, trailhead, multiple_paths=False):
    score = 0
    seen = {trailhead}
    queue = [trailhead]
    while queue:
        place = queue.pop(0)
        place_val = topographic_map[place[0]][place[1]]
        if place_val == 9:
            score += 1
        for new_place in [(place[0] + 1, place[1]), (place[0] - 1, place[1]), (place[0], place[1] + 1), (place[0], place[1] - 1)]:
            if in_bounds(new_place, topographic_map):
                new_place_val = topographic_map[new_place[0]][new_place[1]]
                if (new_place_val - place_val) == 1 and ((not multiple_paths and new_place not in seen) or multiple_paths):
                    queue.append(new_place)
                    seen.add(new_place)
    return score


def main(filename):
    topographic_map = []
    trailheads = []
    with open(filename) as input_f:
        for y_idx, line in enumerate(input_f):
            map_line = []
            for x_idx, char in enumerate(line.strip()):
                num = int(char)
                if num == 0:
                    trailheads.append((y_idx, x_idx))
                map_line.append(num)
            topographic_map.append(map_line)

    total_score = 0
    for trailhead in trailheads:
        total_score += get_score(topographic_map, trailhead, multiple_paths=False)

    total_rating = 0
    for trailhead in trailheads:
        total_rating += get_score(topographic_map, trailhead, multiple_paths=True)

    print(f"Total score: {total_score}")
    print(f"Total rating: {total_rating}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print(f"Usage: {sys.argv[0]} <input.txt>")
        sys.exit(1)
