from itertools import product

with open('input') as f:
    input = f.read().splitlines()

ingredients = []

for line in input:
    _, _, capacity, _, durability, _, flavor, _, texture, _, calories = line.replace(',', '').split(' ')
    ingredients.append((int(capacity), int(durability), int(flavor), int(texture), int(calories)))

r = product(range(100), repeat=len(ingredients))
balances = [x for x in r if sum(x) == 100] 

highest_part_1 = 0
highest_part_2 = 0

recipes = []
for balance in balances:
    recipes.append(list(zip(balance, ingredients)))
 
for recipe in recipes:
    pr = 1

    for i in range(4):
        sum = 0
        for ingredient in recipe:
            sum += ingredient[0] * ingredient[1][i]
            
        pr *= 0 if sum < 0 else sum
    
    calories = 0
    for ingredient in recipe:
        calories += ingredient[0] * ingredient[1][4]

    if pr > highest_part_1: highest_part_1 = pr
    if pr > highest_part_2 and calories == 500: highest_part_2 = pr

print('Part 1:', highest_part_1)
print('Part 2:', highest_part_2)