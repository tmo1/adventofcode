# https://adventofcode.com/2023/day/7

from collections import defaultdict


def hand_type(hand):
    cards = defaultdict(lambda: 0)
    for card in hand:
        cards[card] += 1
    match len(cards):
        case 1:
            return 6
        case 2:
            return 5 if 4 in cards.values() else 4
        case 3:
            return 3 if 3 in cards.values() else 2
        case 4:
            return 1
        case _:
            return 0


card_order = '23456789TJQKA'
hands = open(0).readlines()
hands.sort(key=lambda h: (hand_type(h[:5]), tuple([card_order.index(c) for c in h[:5]])))
print(sum([int(h[6:]) * (i + 1) for i, h in enumerate(hands)]))
