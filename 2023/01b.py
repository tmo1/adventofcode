# https://adventofcode.com/2023/day/1#part2

total = 0
numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
for line in open(0):
    i, first_digit = 0, None
    while i < len(line):
        if str(line[i]).isdigit():
            first_digit = int(line[i])
        else:
            for number, digit in numbers.items():
                if line[i:].startswith(number):
                    first_digit = digit
                    break
        if first_digit is not None:
            break
        i += 1
    i, last_digit = len(line) - 1, None
    while i >= 0:
        if str(line[i]).isdigit():
            last_digit = int(line[i])
        else:
            for number, digit in numbers.items():
                if line[i:].startswith(number):
                    last_digit = digit
                    break
        if last_digit is not None:
            break
        i -= 1
    total += first_digit * 10 + last_digit
print(total)
