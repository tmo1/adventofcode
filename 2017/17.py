# https://adventofcode.com/2017/day/17

buffer, current, steps = [0], 0, int(open(0).readline())
for i in range(1, 2018):
    current = ((current + steps) % i) + 1
    buffer.insert(current, i)
print(buffer[current + 1])
