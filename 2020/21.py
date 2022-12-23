#! /usr/bin/python3

# https://adventofcode.com/2020/day/21

import re

#f = open('aoc-input', 'r')
f = open('sample', 'r')

ing_re = re.compile('(.*)\(contains(.*)\)')
allergens = {}
ing_mentions = {}
while line := f.readline():
	m = ing_re.match(line)
	ingredients = m.group(1).split()
	for ingredient in ingredients:
		if ingredient in ing_mentions:
			ing_mentions[ingredient] += 1
		else:
			ing_mentions[ingredient] = 1
	ingredients = set(ingredients)
	raw_allergens = m.group(2).split()
	a = []
	for allergen in raw_allergens:
		a.append(allergen.translate(allergen.maketrans('', '', ',')))
	for allergen in a:
		if allergen in allergens:
			allergens[allergen] &= ingredients
		else:
			allergens[allergen] = ingredients.copy()

ingredient = 'X'
ingredients = {}
while ingredient:
	ingredient = ''
	for allergen in allergens:
		if len(allergens[allergen]) == 1:
			ingredient = allergens[allergen].pop()
			ingredients[ingredient] = allergen
			for a in allergens:
				allergens[a].discard(ingredient)

total = 0
for ingredient in ing_mentions:
	if not ingredient in ingredients:
		total += ing_mentions[ingredient]
print(total)
