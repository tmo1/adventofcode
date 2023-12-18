# https://adventofcode.com/2023/day/11#part2

image = [[(x, y) if c == '#' else None for x, c in enumerate(line.strip())] for y, line in enumerate(open(0))]
empty_lines = 0
for y, line in enumerate(image):
    if len(set(line)) > 1:
        image[y] = [(n[0], n[1] + empty_lines * 999999) if n is not None else None for n in line]
    else:
        empty_lines += 1
empty_lines = 0
for x in range(len(image[0])):
    line = [image[y][x] for y in range(len(image))]
    if len(set(line)) > 1:
        for y in range(len(image)):
            image[y][x] = (image[y][x][0] + empty_lines * 999999, image[y][x][1]) if image[y][x] is not None else None
    else:
        empty_lines += 1
galaxies = [g for line in image for g in line if g is not None]
lengths = 0
for i, galaxy1 in enumerate(galaxies):
    for galaxy2 in galaxies[i + 1:]:
        lengths += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
print(lengths)
