# https://adventofcode.com/2023/day/3#part2

def is_digit(d):
    return True if 48 <= ord(d) <= 57 else False


def get_part(px, py):
    line = schematics[py]
    begin_part, end_part = px, px
    while begin_part >= 0 and is_digit(line[begin_part]):
        begin_part -= 1
    while end_part < len(line) and is_digit(line[end_part]):
        end_part += 1
    return int(line[begin_part + 1:end_part])


schematics = [line.strip() for line in open(0)]
total = 0
for y, line in enumerate(schematics):
    for x, c in enumerate(line):
        if c == '*':
            parts = []
            if y > 0:
                if x > 0:
                    if is_digit(schematics[y - 1][x - 1]):
                        parts.append(get_part(x - 1, y - 1))
                        if (not is_digit(schematics[y - 1][x])) and x < len(line) - 1 and is_digit(schematics[y - 1][x + 1]):
                            parts.append(get_part(x + 1, y - 1))
                    else:
                        if is_digit(schematics[y - 1][x]):
                            parts.append(get_part(x, y - 1))
                        elif x < len(line) - 1 and is_digit(schematics[y - 1][x + 1]):
                            parts.append(get_part(x + 1, y - 1))
            if y < len(schematics) - 1:
                if x > 0:
                    if is_digit(schematics[y + 1][x - 1]):
                        parts.append(get_part(x - 1, y + 1))
                        if (not is_digit(schematics[y + 1][x])) and x < len(line) - 1 and is_digit(schematics[y + 1][x + 1]):
                            parts.append(get_part(x + 1, y + 1))
                    else:
                        if is_digit(schematics[y + 1][x]):
                            parts.append(get_part(x, y + 1))
                        elif x < len(line) - 1 and is_digit(schematics[y + 1][x + 1]):
                            parts.append(get_part(x + 1, y + 1))
            if x > 0 and is_digit(line[x - 1]):
                parts.append(get_part(x - 1, y))
            if x < len(line) - 1 and is_digit(line[x + 1]):
                parts.append(get_part(x + 1, y))
            if len(parts) == 2:
                total += parts[0] * parts[1]
print(total)
