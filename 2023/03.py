# https://adventofcode.com/2023/day/3

schematics = [line.strip() for line in open(0)]
total = 0
for y, line in enumerate(schematics):
    x = 0
    while x < len(schematics[0]):
        if 48 <= ord(line[x]) <= 57:
            x_end = x + 1
            while x_end < len(line) and 48 <= ord(line[x_end]) <= 57:
                x_end += 1
            engine_part = False
            for y1 in range(max(y - 1, 0), min(y + 2, len(schematics))):
                for x1 in range(max(x - 1, 0), min(x_end + 1, len(line))):
                    if not (48 <= ord(schematics[y1][x1]) <= 57) and schematics[y1][x1] != '.':
                        engine_part = True
                        break
                if engine_part:
                    break
            if engine_part:
                total += int(line[x:x_end])
            x = x_end
        x += 1
print(total)
