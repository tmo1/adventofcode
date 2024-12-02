# https://adventofcode.com/2024/day/2#part2

def is_safe(r):
    if r[0] > r[1]:
        r.reverse()
    for i in range(len(r) - 1):
        if not 1 <= r[i + 1] - r[i] <= 3:
            return False
    return True


safe = 0
for report in open(0):
    report = [int(x) for x in report.split()]
    if is_safe(report):
        safe += 1
    else:
        for level in range(len(report)):
            if is_safe(report[:level] + report[level + 1:]):
                safe += 1
                break
print(safe)
