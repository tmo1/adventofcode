# https://adventofcode.com/2024/day/8

frequencies, antinodes = [[] for n in range(75)], set()
for  y, line in enumerate(open(0)):
    for x, c in enumerate(line.strip()):
        if c != '.':
            frequencies[ord(c) - 48].append((x, y))
for frequency in frequencies:
    for i, antenna1 in enumerate(frequency):
        for antenna2 in frequency[i + 1:]:
            antinodes |= {(antenna1[0] * 2 - antenna2[0], antenna1[1] * 2 - antenna2[1]), (antenna2[0] * 2 - antenna1[0], antenna2[1] * 2 - antenna1[1])}
            if (antenna1[0] - antenna2[0]) % 3 == 0 and (antenna1[1] - antenna2[1]) % 3 == 0:
                dx, dy = (antenna1[0] - antenna2[0]) // 3, (antenna1[1] - antenna2[1]) // 3
                antinodes |= {(antenna1[0] - dx, antenna1[1] - dy), (antenna1[0] - 2 * dx, antenna1[1] - 2 * dy)}
print(sum([1 for antinode in antinodes if 0 <= antinode[0] < y + 1 and 0 <= antinode[1] < y + 1]))
