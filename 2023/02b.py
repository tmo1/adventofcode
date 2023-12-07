# https://adventofcode.com/2023/day/2#part2

power_sum = 0
for line in open(0):
    color_table = {'red': 0, 'green': 0, 'blue': 0}
    game, cubes = line.split(': ')
    grabs = cubes.split('; ')
    for grab in grabs:
        colors = grab.split(', ')
        for color in colors:
            color_num, color_name = color.split()
            color_table[color_name] = max(color_table[color_name], int(color_num))
    power = 1
    for number in color_table.values():
        power *= number
    power_sum += power
print(power_sum)
