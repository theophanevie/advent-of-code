from collections import defaultdict
from functools import reduce
from random import choice
from sys import argv

food = []
with open(argv[1], "r") as f:
    for line in f.readlines():
        l = [l.split() for l in line.replace("(", "").replace(")", "").replace(",", "").strip().split("contains")]
        food.append(l)

occurrence = defaultdict(dict)
all_ingredients = []

for f in food:
    ingredients, allergens = f
    all_ingredients += ingredients

    for allergen in allergens:
        for ingredient in ingredients:
            if ingredient not in occurrence[allergen]:
                occurrence[allergen][ingredient] = 1
            else:
                occurrence[allergen][ingredient] += 1

# Filter out any ingredient that does not appear frequently enough to match the quantity of allergen occurrences.
for allergen in occurrence:
    cur_max = max(list(occurrence[allergen].values()))
    to_del = []

    for ingredient in occurrence[allergen]:
        if occurrence[allergen][ingredient] < cur_max:
            to_del.append(ingredient)

    for ingredient in to_del:
        del occurrence[allergen][ingredient]


ingredients_with_allergens = set(reduce(lambda a, b : a + b, [list(v.keys()) for _, v in occurrence.items()]))
safe_ingredients = set(all_ingredients) - ingredients_with_allergens

part1 = sum([all_ingredients.count(i) for i in safe_ingredients])
print(f"Part 1: {part1}")


allergens_count = len(occurrence)
correspondence = {}


while len(occurrence) > 0:
    min_match = None
    for allergen in occurrence:
        if min_match is None or len(occurrence[allergen]) < len(occurrence[min_match]):
            min_match = allergen

    ingredient = choice(list(occurrence[min_match].keys()))
    correspondence[ingredient] = min_match

    for allergen in occurrence:
        if ingredient in occurrence[allergen]:
            del occurrence[allergen][ingredient]
    del occurrence[min_match]

part2 = list(correspondence.keys())
part2.sort(key=lambda x: correspondence[x])
print(f"Part 2: {",".join(part2)}")
