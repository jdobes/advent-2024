import sys

ORIGINAL_MAP = []
ORIGINAL_POS = [0, 0]

STATE = {
    "map": None,
    "pos": None,
    "direction": None,
    "visited": None,
    "cycle_detected": None
}


def reset_state():
    STATE["map"] = []
    for row in ORIGINAL_MAP:
        STATE["map"].append(row.copy())
    STATE["pos"] = [ORIGINAL_POS[0], ORIGINAL_POS[1]]
    STATE["direction"] = "^"
    STATE["visited"] = set()
    STATE["cycle_detected"] = False


def pos_in_map(pos):
    return pos[0] >= 0 and pos[0] < len(STATE["map"]) and pos[1] >= 0 and pos[1] < len(STATE["map"][0])


def pos_is_obstacle(pos):
    return STATE["map"][pos[0]][pos[1]] in ["#", "O"]


def next_direction():
    if STATE["direction"] == "^":
        STATE["direction"] = ">"
    elif STATE["direction"] == ">":
        STATE["direction"] = "v"
    elif STATE["direction"] == "v":
        STATE["direction"] = "<"
    else:  # <
        STATE["direction"] = "^"


def step():
    old_pos = STATE["pos"]
    new_pos = None
    tries = 0
    while not new_pos or tries >= 4:
        tries += 1
        if STATE["direction"] == "^":
            new_pos_cand = (old_pos[0] - 1, old_pos[1])
        elif STATE["direction"] == ">":
            new_pos_cand = (old_pos[0], old_pos[1] + 1)
        elif STATE["direction"] == "v":
            new_pos_cand = (old_pos[0] + 1, old_pos[1])
        else:  # <
            new_pos_cand = (old_pos[0], old_pos[1] - 1)

        if pos_in_map(new_pos_cand) and not pos_is_obstacle(new_pos_cand):
            new_pos = new_pos_cand
        elif pos_in_map(new_pos_cand):  # change direction
            next_direction()
        else:  # out of map
            new_pos = new_pos_cand

    if new_pos:
        STATE["map"][old_pos[0]][old_pos[1]] = "X"
        STATE["pos"] = new_pos

        if (new_pos[0], new_pos[1], STATE["direction"]) not in STATE["visited"]:
            STATE["visited"].add((new_pos[0], new_pos[1], STATE["direction"]))
        else:
            STATE["cycle_detected"] = True
    else:
        print("Unable to find a path! (should not happen)")
        sys.exit(1)


def count_path():
    cnt = 0
    for row in STATE["map"]:
        for col in row:
            if col == "X":
                cnt += 1
    return cnt


def main(filename):
    with open(filename) as input_f:
        for idx, line in enumerate(input_f):
            ORIGINAL_MAP.append(list(line.strip()))
            if "^" in line:
                ORIGINAL_POS[0] = idx
                ORIGINAL_POS[1] = line.index("^")

    reset_state()
    while pos_in_map(STATE["pos"]):
        step()
    print(f"Traveled: {count_path()}")

    detected_cycles = 0
    for row in range(len(ORIGINAL_MAP)):
        for col in range(len(ORIGINAL_MAP[row])):
            reset_state()
            STATE["map"][row][col] = "O"
            while pos_in_map(STATE["pos"]) and not STATE["cycle_detected"]:
                step()
            if STATE["cycle_detected"]:
                detected_cycles += 1
    print(f"Detected cycles: {detected_cycles}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print(f"Usage: {sys.argv[0]} <input.txt>")
        sys.exit(1)
