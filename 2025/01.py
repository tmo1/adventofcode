# https://adventofcode.com/2025/day/1

position, combination = 50, 0
for line in open(0):
    position += -int(line[1:]) if line[0] == 'L' else int(line[1:])
    if position % 100 == 0: combination += 1
print(combination)
