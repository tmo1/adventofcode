# https://adventofcode.com/2024/day/13
# This code does not check for multi-solution machines - it will presumably throw a 'ZeroDivisionError' on such machines
# It works for my input, which apparently doesn't contain any such machines
# https://old.reddit.com/r/adventofcode/comments/1hd4wda/2024_day_13_solutions/m1vvrx5/
# https://old.reddit.com/r/adventofcode/comments/1hdh06e/2024_day_13_both_parts_is_eric_being_supersneaky/

machines, total = open(0).readlines(), 0
for i in range(0, len(machines), 4):
    a = [int(n) for n in machines[i][12:].split(', Y+')]
    b = [int(n) for n in machines[i + 1][12:].split(', Y+')]
    p = [int(n) for n in machines[i + 2][9:].split(', Y=')]
    p, q = (b[1] * p[0] - b[0] * p[1]) / (a[0] * b[1] - a[1] * b[0]), (a[1] * p[0] - a[0] * p[1]) / (b[0] * a[1] - a[0] * b[1])
    if float.is_integer(p) and float.is_integer(q): total += int(p) * 3 + int(q)
print(total)
