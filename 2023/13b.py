# https://adventofcode.com/2023/day/13


def find_reflection_line(first_axis, first_n):
    for i in range(1, len(pattern)):
        reflect_range = min(i, len(pattern) - i)
        for j in range(1, reflect_range + 1):
            if pattern[i - j] != pattern[i + j - 1]:
                break
        else:
            if first_axis is None or first_axis != 'h' or first_n != i:
                return 'h', i
    for i in range(1, len(pattern[0])):
        reflect_range = min(i, len(pattern[0]) - i)
        for j in range(1, reflect_range + 1):
            if [pattern[k][i - j] for k in range(len(pattern))] != [pattern[k][i + j - 1] for k in range(len(pattern))]:
                break
        else:
            if first_axis is None or first_axis != 'v' or first_n != i:
                return 'v', i
    return None, None


pattern = []
fh = open(0)
total = 0
while True:
    line = fh.readline()
    if line == '\n' or line == '':
        axis, n = find_reflection_line(None, None)
        for y, row in enumerate(pattern):
            for x, c in enumerate(row):
                pattern[y][x] = '.' if c == '#' else '#'
                new_axis, new_n = find_reflection_line(axis, n)
                if new_axis is not None:
                    total += 100 * new_n if new_axis == 'h' else new_n
                    break
                pattern[y][x] = c
            else:
                continue
            break
        if line == '':
            print(total)
            quit()
        pattern = []
    else:
        pattern.append(list(line.strip()))
