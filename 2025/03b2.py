# https://adventofcode.com/2025/day/3#part2

joltage = 0
for line in open(0):
    bank, current_battery = [int(n) for n in line[:-1]], -1
    for i in range(12):
        next_battery = max(range(current_battery + 1, len(bank) - 11 + i), key=lambda x: (bank[x], -x))
        joltage, current_battery = joltage + bank[next_battery] * 10 ** (11 - i), next_battery
print(joltage)