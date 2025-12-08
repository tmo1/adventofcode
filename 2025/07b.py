# https://adventofcode.com/2025/day/7#part2

def timelines(x, y):
    if y == len(manifold): return 1
    if not isinstance(manifold[y][x], int):
        manifold[y][x] = timelines(x, y + 1) if manifold[y][x] == '.' else timelines(x - 1, y + 1) + timelines(x + 1, y + 1)
    return manifold[y][x]

manifold = [list(line) for line in open(0)]
print(timelines(manifold[0].index('S'), 1))
