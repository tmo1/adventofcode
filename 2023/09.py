# https://adventofcode.com/2023/day/9

total = 0
for line in open(0):
    report = [[int(x) for x in line.split()]]
    while len([n for n in report[-1] if n == 0]) < len(report[-1]):
        report.append([report[-1][i + 1] - report[-1][i] for i in range(len(report[-1]) - 1)])
    for i in range(len(report) - 2, -1, -1):
        report[i].append(report[i][-1] + report[i + 1][-1])
    total += report[0][-1]
print(total)
