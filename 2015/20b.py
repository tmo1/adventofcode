# https://adventofcode.com/2015/day/20#part2
# this gives the right answer in about 29 seconds on my w550s

puzzle_input = 36000000
num = 0
houses = {}
first = puzzle_input
while True:
    num += 1
    if num >= first:
        print(first)
        exit()
    # print(num)
    for i in range(1, 51):
        house = num * i
        if house in houses:
            houses[house] += num * 11
        else:
            houses[house] = num * 11
        if houses[house] >= puzzle_input and house < first:
            first = house
