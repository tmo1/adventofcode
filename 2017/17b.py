# https://adventofcode.com/2017/day/17#part2

current, steps, n = 0, int(open(0).readline()), 0
for i in range(1, 50000001):
    current = ((current + steps) % i)
    if current == 0:
        n = i
    current += 1
print(n)
