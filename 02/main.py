import sys


def is_report_safe(report):
    increasing = report[1] > report[0]
    prev_level = report[0]
    for level in report[1:]:
        diff = level - prev_level
        if ((increasing and level > prev_level) or (not increasing and level < prev_level)) and 1 <= abs(diff) <= 3:
            prev_level = level
        else:
            return False
    return True


def del_one_level(report):
    all_modified_reports = []
    for idx in range(len(report)):
        modified_report = report.copy()
        del modified_report[idx]
        all_modified_reports.append(modified_report)
    return all_modified_reports


def main(filename):
    safe_reports = 0
    safe_reports_toleration = 0
    with open(filename) as input_f:
        for line in input_f:
            report = line.split()
            report = [int(num) for num in report]
            if is_report_safe(report):
                safe_reports += 1
                safe_reports_toleration += 1
            elif any(is_report_safe(rep) for rep in del_one_level(report)):
                safe_reports_toleration += 1

    print(f"Safe reports: {safe_reports}")
    print(f"Safe reports with toleration: {safe_reports_toleration}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print(f"Usage: {sys.argv[0]} <input.txt>")
        sys.exit(1)
