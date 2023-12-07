# https://adventofcode.com/2023/day/2

id_sum = 0
color_table = {'red': 12, 'green': 13, 'blue': 14}
for line in open(0):
    flag = True
    game, cubes = line.split(': ')
    grabs = cubes.split('; ')
    for grab in grabs:
        colors = grab.split(', ')
        for color in colors:
            color_num, color_name = color.split()
            if color_table[color_name] < int(color_num):
                flag = False
                break
        if not flag:
            break
    if flag:
        id_sum += int(game.split()[1])
print(id_sum)
