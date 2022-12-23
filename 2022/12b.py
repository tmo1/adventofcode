# https://adventofcode.com/2022/day/12#part2

import sys

heights = [list(line.strip()) for line in sys.stdin]
y_len = len(heights)
x_len = len(heights[0])
for y in range(y_len):
    for x in range(x_len):
        letter = heights[y][x]
        if letter == 'E':
            end_y = y
            end_x = x
            letter = 'z'
            distance = 0
        else:
            distance = y_len * x_len
        if letter == 'S':
            letter = 'a'
        heights[y][x] = {'distance': distance, 'elevation': ord(letter), 'visited': False}
while True:
    cur_y = cur_x = -1
    min_distance = y_len * x_len
    for y in range(y_len):
        for x in range(x_len):
            if heights[y][x]['visited'] is False and heights[y][x]['distance'] < min_distance:
                cur_y = y
                cur_x = x
                min_distance = heights[y][x]['distance']
    if cur_y == -1:
        min_distance = y_len * x_len
        ord_a = ord('a')
        for y in range(y_len):
            for x in range(x_len):
                if heights[y][x]['elevation'] == ord_a:
                    min_distance = min(min_distance, heights[y][x]['distance'])
        print(min_distance)
        quit()
    for y in range(max(cur_y - 1, 0), min(cur_y + 2, y_len)):
        for x in range(max(cur_x - 1, 0), min(cur_x + 2, x_len)):
            if ((y != cur_y and x == cur_x) or (y == cur_y and x != cur_x)) and heights[y][x]['elevation'] >= \
                    heights[cur_y][cur_x]['elevation'] - 1 and \
                    heights[y][x]['distance'] > heights[cur_y][cur_x]['distance'] + 1:
                heights[y][x]['distance'] = heights[cur_y][cur_x]['distance'] + 1
    heights[cur_y][cur_x]['visited'] = True
