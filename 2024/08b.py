# https://adventofcode.com/2024/day/8#part2

def calc(a, b, dx, dy):
    while True:
        if not (0 <= a < y + 1 and 0 <= b < y + 1):
            return
        antinodes.add((a, b))
        a, b = a + dx, b + dy

frequencies, antinodes = [[] for n in range(75)], set()
for  y, line in enumerate(open(0)):
    for x, c in enumerate(line.strip()):
        if c != '.':
            frequencies[ord(c) - 48].append((x, y))
for frequency in frequencies:
    for i, antenna1 in enumerate(frequency):
        for antenna2 in frequency[i + 1:]:
            dx, dy = antenna1[0] - antenna2[0], antenna1[1] - antenna2[1]
            calc(antenna1[0], antenna1[1], dx, dy), calc(antenna1[0], antenna1[1], -dx, -dy), calc(antenna2[0], antenna2[1], dx, dy), calc(antenna2[0], antenna2[1], -dx, -dy)
print(len(antinodes))
