# https://adventofcode.com/2015/day/20
# this gives the right answer, but takes almost 5 minutes on my w550s

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
    for i in range(num, first, num):
        if i in houses:
            houses[i] += num * 10
        else:
            houses[i] = num * 10
        if houses[i] >= puzzle_input and i < first:
            first = i
