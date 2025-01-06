# https://adventofcode.com/2024/day/19

maze = open(0).read()
m_start, m_end = maze.find('S'), maze.find('E')
maze = [list(line) for line in maze.split()]
x_len = len(maze) + 1
x_start, y_start, x_end, y_end, x_prev, y_prev = m_start % x_len, m_start // x_len, m_end % x_len, m_end // x_len, -1, -1
x, y, directions = x_start, y_start, {(1, 0), (-1, 0), (0, 1), (0, -1)}
maze[y][x] = 0
while x != x_end or y != y_end:
    for direction in directions:
        x1, y1 = x + direction[0], y + direction[1]
        if maze[y1][x1] != '#' and (x1 != x_prev or y1 != y_prev):
            x, y, x_prev, y_prev = x1, y1, x, y
            break
    maze[y][x] = maze[y_prev][x_prev] + 1
total = 0
for y in range(1, len(maze) - 1):
    for x in range(1, len(maze[0]) - 1):
        if maze[y][x] != '#':
            for direction in directions:
                x1, y1 = x + direction[0], y + direction[1]
                if maze[y1][x1] == '#' and 0 < y1 < len(maze) - 1 and 0 < x1 < len(maze[0]) - 1:
                    for direction2 in directions:
                        x2, y2 = x1 + direction2[0], y1 + direction2[1]
                        if maze[y2][x2] != '#' and maze[y2][x2] - maze[y][x] >= 102: total += 1
print(total)
