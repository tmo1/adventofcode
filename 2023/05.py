# https://adventofcode.com/2023/day/5

puzzle = open(0)
numbers = [int(n) for n in puzzle.readline().split()[1:]]
new_numbers = []
line = puzzle.readline()
while line:
    if line == '\n':
        numbers = [n for n in numbers if n is not None] + new_numbers
        new_numbers = []
        puzzle.readline()
    else:
        dest_start, src_start, range_length = [int(n) for n in line.split()]
        for i in range(len(numbers)):
            if numbers[i] is not None and src_start <= numbers[i] < src_start + range_length:
                new_numbers.append(dest_start + numbers[i] - src_start)
                numbers[i] = None
    line = puzzle.readline()
print(min([n for n in numbers if n is not None] + new_numbers))
