# https://adventofcode.com/2024/day/2

safe = 0
for report in open(0):
    report = [int(x) for x in report.split()]
    if report[0] > report[1]:
        report.reverse()
    for i in range(len(report) - 1):
        if not 1 <= report[i + 1] - report[i] <= 3:
            break
    else:
        safe += 1
print(safe)
