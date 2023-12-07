# https://adventofcode.com/2023/day/7#part2

card_order = 'J23456789TQKA'


def hand_type(hand):
    first_joker = hand.find('J')
    if first_joker > -1:
        return max([hand_type(hand[:first_joker] + joker_value + hand[first_joker + 1:]) for joker_value in card_order[1:]])
    cards = {}
    for card in hand:
        cards[card] = cards[card] + 1 if card in cards else 1
    if len(cards) == 1:
        return 6
    if len(cards) == 2:
        return 5 if 4 in cards.values() else 4
    if len(cards) == 3:
        return 3 if 3 in cards.values() else 2
    if len(cards) == 4:
        return 1
    return 0


hands = open(0).readlines()
hands.sort(key=lambda h: (hand_type(h[:5]), tuple([card_order.index(c) for c in h[:5]])))
print(sum([int(h[6:]) * (i + 1) for i, h in enumerate(hands)]))
