# https://adventofcode.com/2025/day/3#part2

def get_next_digit(digit, place, combination):
    global bank
    next_battery = max(d for d in batteries[place:len(batteries) - 11 + digit])
    if digit == 11:
        bank = max(bank, combination + next_battery)
        return
    next_combination, next_digit = combination + next_battery * 10 ** (11 - digit), digit + 1
    for next_place in (p for p in range(place, len(batteries) - 11 + digit) if batteries[p] == next_battery):
        get_next_digit(next_digit, next_place + 1, next_combination)


joltage = 0
for line in open(0):
    batteries, bank = [int(n) for n in line[:-1]], 0
    get_next_digit(0, 0, 0)
    joltage += bank
print(joltage)