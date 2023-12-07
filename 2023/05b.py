# https://adventofcode.com/2023/day/5#part2

puzzle = open(0)
numbers = [int(n) for n in puzzle.readline().split()[1:]]
numbers = [(numbers[i], numbers[i] + numbers[i + 1]) for i in range(0, len(numbers), 2)]
new_numbers = []
line = puzzle.readline()
while line:
    if line == '\n':
        numbers = [n for n in numbers if n is not None] + new_numbers
        new_numbers = []
        puzzle.readline()
    else:
        dest_start, src_start, range_length = [int(n) for n in line.split()]
        i = 0
        while i < len(numbers):
            current_range = numbers[i]
            if current_range is not None and current_range[1] >= src_start + 1 and current_range[0] < src_start + range_length:
                mapped_range = (dest_start + max(current_range[0], src_start) - src_start, dest_start + min(current_range[1], src_start + range_length) - src_start)
                new_numbers.append(mapped_range)
                if current_range[0] < src_start:
                    numbers.append((current_range[0], src_start))
                if current_range[1] > src_start + range_length:
                    numbers.append((src_start + range_length, current_range[1]))
                numbers[i] = None
            i += 1
    line = puzzle.readline()
print(min([n for n in numbers if n is not None] + new_numbers)[0])
