# https://adventofcode.com/2015/day/15#part2

import sys

ingredients = []
for line in sys.stdin:
    words = [(x.strip(',')) for x in line.split()]
    ingredients.append([int(words[2]), int(words[4]), int(words[6]), int(words[8]), int(words[10])])
high_score = 0


def add_ingredient(spoons, partial_scores, i, calories):
    global high_score
    new_partial_scores = [0, 0, 0, 0]
    if i == len(ingredients) - 1:
        n = 100 - spoons
        if calories + (n * ingredients[i][4]) != 500:
            return
        for j in range(4):
            new_partial_scores[j] = partial_scores[j] + (n * ingredients[i][j])
        total_score = 1
        for j in range(4):
            if new_partial_scores[j] <= 0:
                return
            total_score *= new_partial_scores[j]
        if total_score > high_score:
            high_score = total_score
    else:
        for j in range(101 - spoons):
            for k in range(4):
                new_partial_scores[k] = partial_scores[k] + (j * ingredients[i][k])
            add_ingredient(spoons + j, new_partial_scores, i + 1, calories + (j * ingredients[i][4]))


add_ingredient(0, [0, 0, 0, 0], 0, 0)
print(high_score)
