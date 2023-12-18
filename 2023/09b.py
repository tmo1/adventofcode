# https://adventofcode.com/2023/day/9#part2

total = 0
for line in open(0):
    report = [[int(x) for x in line.split()]]
    while len([n for n in report[-1] if n == 0]) < len(report[-1]):
        report.append([report[-1][i + 1] - report[-1][i] for i in range(len(report[-1]) - 1)])
    for i in range(len(report) - 2, -1, -1):
        report[i] = [report[i][0] - report[i + 1][0]] + report[i]
    total += report[0][0]
print(total)
