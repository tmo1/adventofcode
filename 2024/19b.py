# https://adventofcode.com/2024/day/19#part2

def arrange(x):
    if len(x) == 1: return 1 if x in towels else 0
    if len(x) == 0: return 1
    if x in sub_designs: return sub_designs[x]
    midpoint = len(x) // 2
    total = arrange(x[:midpoint]) * arrange(x[midpoint:])
    for towel in towels:
        if 1 < len(towel) <= len(x):
           for i in range(len(towel) - 1):
                if x[midpoint - 1 - i:midpoint - 1 - i + len(towel)] == towel: total += arrange(x[:midpoint - 1 - i]) * arrange(x[midpoint - 1 - i + len(towel):])
    sub_designs[x] = total
    return total

towels, designs = open(0).read().split('\n\n')
towels = towels.split(', ')
sub_designs = {}
print(sum([arrange(design) for design in designs.split()]))
