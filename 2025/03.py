# https://adventofcode.com/2025/day/3

joltage = 0
for line in open(0):
    bank = 0
    for i, n in enumerate(line[:-1]):
        for j, m in enumerate(line[i + 1:-1], start=i + 1):
            bank = max(int(n) * 10 + int(m), bank)
    joltage += bank
print(joltage)