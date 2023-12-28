# https://adventofcode.com/2023/day/18#part2

h_lines, v_lines, x, y = [], [], 0, 0
for line in open(0):
    line = line.split()
    n = int(line[2][2:7], 16)
    match line[2][7]:
        case '0':
            h_lines.append((x, x + n, y))
            x += n
        case '1':
            v_lines.append((y, y + n, x))
            y += n
        case '2':
            h_lines.append((x - n, x, y))
            x -= n
        case '3':
            v_lines.append((y - n, y, x))
            y -= n
h_bars = sorted({h_line[2] for h_line in h_lines})
v_bars = sorted({v_line[2] for v_line in v_lines})
total = 0
cells = []
for y in range(len(h_bars) - 1):
    cell_row = []
    h_bar_prev = h_bars[y]
    h_bar = h_bars[y + 1]
    for x in range(len(v_bars) - 1):
        v_bar_left = False
        for v_line in v_lines:
            if h_bar_prev >= v_line[0] and h_bar <= v_line[1] and v_bars[x] == v_line[2]:
                v_bar_left = True
                break
        prev_in = False if (x == 0 or not cell_row[x - 1]) else True
        if prev_in != v_bar_left:
            cell_row.append(True)
            total += (h_bar - h_bar_prev - 1) * (v_bars[x + 1] - v_bars[x] - 1)
            if prev_in:
                total += h_bar - h_bar_prev - 1
            if y > 0 and cells[y - 1][x]:
                total += v_bars[x + 1] - v_bars[x] - 1
            if prev_in and not v_bar_left and y > 0 and cells[y - 1][x] and cells[y - 1][x - 1]:
                total += 1
        else:
            cell_row.append(False)
    cells.append(cell_row)
print(total + sum([v_line[1] - v_line[0] + 1 for v_line in v_lines]) + sum([h_line[1] - h_line[0] + 1 for h_line in h_lines]) - len(v_lines) - len(h_lines))
