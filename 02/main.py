import sys


def main(filename):
    safe_reports = 0
    with open(filename) as input_f:
        for line in input_f:
            report = line.split()
            if int(report[0]) == int(report[1]):
                continue
            increasing = int(report[1]) > int(report[0])
            prev_level = int(report[1])
            safe_report = True
            for level_s in report[2:]:
                level = int(level_s)
                diff = abs(level - prev_level)
                if ((increasing and level > prev_level) or (not increasing and level < prev_level)) and diff <= 3:
                    prev_level = level
                else:
                    safe_report = False
                    break
            if safe_report:
                print(f"Safe: {report}")
                safe_reports += 1
            else:
                print(f"Unsafe: {report}")
    print(f"Safe reports: {safe_reports}")
            


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print(f"Usage: {sys.argv[0]} <input.txt>")
        sys.exit(1)
