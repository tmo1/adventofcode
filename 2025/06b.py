# https://adventofcode.com/2025/day/6#part2

from math import prod
lines = open(0).readlines()
total, column, numbers = 0, len(lines[0]) - 2, []
while column >= 0:
    while True:
        numbers.append(int(''.join([line[column] for line in lines[:-1]])))
        if lines[-1][column] == ' ': column -= 1
        else:
            total, numbers, column = total + (sum(numbers) if lines[-1][column] == '+' else prod(numbers)), [], column - 2
            break
print(total)
