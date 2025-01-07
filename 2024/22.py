# https://adventofcode.com/2024/day/22

total = 0
for number in open(0):
    number = int(number)
    for i in range(2000):
        number = (number ^ (number * 64)) % 16777216
        number = (number ^ (number // 32)) % 16777216
        number = (number ^ (number * 2048)) % 16777216
    total += number
print(total)
