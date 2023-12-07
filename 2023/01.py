# https://adventofcode.com/2023/day/1

total = 0
for line in open(0):
    digits = [c for c in line if str(c).isdigit()]
    total += int(digits[0] + digits[-1])
print(total)
