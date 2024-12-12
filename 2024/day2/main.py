DECREASING = 0
INCREASING = 1
    
def is_safe(report):
    # levels are all increasing or all decreasing
    # adjacent levels differ by at least one and at most three
    if len(report) == 1:
        return 1 
    
    direction = INCREASING if (report[1] - report[0]) > 0 else DECREASING
    prev_level = None
    for level in report:
        if prev_level == None:
            prev_level = level
            continue

        diff = level - prev_level
        if abs(diff) < 1 or abs(diff) > 3:
            return 0 
        if direction == INCREASING and diff < 0:
            return 0 
        elif direction == DECREASING and diff > 0:
            return 0
        prev_level = level

    return 1

def is_safe_part_2(report):
    if is_safe(report):
        return 1
    
    # Try dropping each level and re-checking 
    for i in range(len(report)):
        if is_safe(report[:i] + report[i+1:]):
            return 1

    return 0

with open("in.txt") as f:
    reports = []
    for line in f.readlines():
        reports.append([int(level) for level in line.strip().split(' ')])

    report_safety = [is_safe_part_2(report) for report in reports]
    print(sum(report_safety))
            


