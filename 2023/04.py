# https://adventofcode.com/2023/day/4

points = 0
for line in open(0):
    win, have = line.split('| ')
    win = {int(n) for n in win.split()[2:]}
    have = {int(n) for n in have.split()}
    matches = len(have & win)
    if matches > 0:
        points += 2 ** (matches - 1)
print(points)
