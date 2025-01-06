# https://adventofcode.com/2024/day/19

def arrange(i, design):
    if i == len(design): return True
    for towel in towels:
        if i + len(towel) <= len(design) and design[i:i + len(towel)] == towel and arrange(i + len(towel), design): return True
    return False

towels, designs = open(0).read().split('\n\n')
towels = towels.split(', ')
print(sum([1 for design in designs.split() if arrange(0, design)]))
