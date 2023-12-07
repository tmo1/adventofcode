# https://adventofcode.com/2023/day/4#part2

cards = open(0).readlines()
copies = [1 for card in cards]
for i, card in enumerate(cards):
    win, have = card.split('| ')
    win = {int(n) for n in win.split()[2:]}
    have = {int(n) for n in have.split()}
    matches = len(have & win)
    for j in range(i + 1, i + 1 + len(have & win)):
        copies[j] += copies[i]
print(sum(copies))
