# https://adventofcode.com/2023/day/11

image = []
for line in open(0):
    image.append(line.strip())
    if '#' not in line:
        image.append('.' * len(image[0]))
i = 0
while i < len(image[0]):
    if '#' not in [line[i] for line in image]:
        for j in range(len(image)):
            image[j] = image[j][:i] + '.' + image[j][i:]
        i += 1
    i += 1
galaxies = [(x, y) for x in range(len(image[0])) for y in range(len(image)) if image[y][x] == '#']
print(galaxies)
lengths = 0
for i, galaxy1 in enumerate(galaxies):
    for galaxy2 in galaxies[i + 1:]:
        lengths += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
print(lengths)
