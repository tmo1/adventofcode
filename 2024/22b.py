# https://adventofcode.com/2024/day/22#part2

sequences = {}
for number in open(0):
    number = int(number)
    monkey, monkey_sequences = [(number % 10, None)], set()
    for i in range(2000):
        number = (number ^ (number * 64)) % 16777216
        number = (number ^ (number // 32)) % 16777216
        number = (number ^ (number * 2048)) % 16777216
        price = number % 10
        monkey.append((price, price - monkey[i][0]))
        if i >= 3:
            sequence = tuple([monkey[j][1] for j in range(i - 2, i + 2)])
            if sequence not in monkey_sequences:
                monkey_sequences.add(sequence)
                sequences[sequence] = sequences[sequence] + [price] if sequence in sequences else [price]
print(max([sum(sequence) for sequence in sequences.values()]))
