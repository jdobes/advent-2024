import sys


def defrag_one_block(filesystem):
    moving_from = len(filesystem) - 1
    while moving_from >= 0:
        if filesystem[moving_from] != ".":
            break
        moving_from -= 1
    moving_to = 0
    while moving_to < moving_from:
        if filesystem[moving_to] == ".":
            filesystem[moving_to] = filesystem[moving_from]
            filesystem[moving_from] = "."
            return True
        moving_to += 1
    return False


def to_flat(filesystem_files):
    filesystem = []
    for file in filesystem_files:
        for x in file:
            filesystem.append(x)
    return filesystem


def defrag_one_file(filesystem, state):
    moving_from = state["moving_from"]
    while True:
        if moving_from < 0:
            break
        while moving_from >= 0:
            file = set(filesystem[moving_from])
            if len(file) == 1 and list(file)[0] != ".":
                break  # Found file
            moving_from -= 1

        moving_to = 0
        while moving_to < moving_from:
            free_space = len([x for x in filesystem[moving_to] if x == "."])
            if free_space >= len(filesystem[moving_from]):
                from_idx = 0
                from_len = len(filesystem[moving_from])
                for to_idx in range(len(filesystem[moving_to])):
                    if from_idx >= from_len:
                        break
                    if filesystem[moving_to][to_idx] == ".":
                        filesystem[moving_to][to_idx] = filesystem[moving_from][from_idx]
                        filesystem[moving_from][from_idx] = "."
                        from_idx += 1
                state["moving_from"] = moving_from
                return True
            moving_to += 1
        moving_from -=1
    return False


def get_checksum(filesystem):
    checksum = 0
    for idx in range(len(filesystem)):
        if filesystem[idx] != ".":
            checksum += idx * filesystem[idx]
    return checksum


def main(filename):
    filesystem = []
    filesystem_files = []
    writing_file = True
    file_id = 0
    with open(filename) as input_f:
        for line in input_f:
            for char in line.strip():
                num = int(char)
                if writing_file:
                    file = []
                    for _ in range(num):
                        file.append(file_id)
                    if file:
                        filesystem.extend(file)
                        filesystem_files.append(file)
                        file_id += 1
                else:
                    free_space = []
                    for _ in range(num):
                        free_space.append(".")
                    if free_space:
                        filesystem.extend(free_space)
                        filesystem_files.append(free_space)
                writing_file = not writing_file

    while defrag_one_block(filesystem):
        pass

    state = {"moving_from": len(filesystem_files) - 1}
    while defrag_one_file(filesystem_files, state):
        pass

    print(f"Checksum: {get_checksum(filesystem)}")
    print(f"Checksum whole files: {get_checksum(to_flat(filesystem_files))}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print(f"Usage: {sys.argv[0]} <input.txt>")
        sys.exit(1)
