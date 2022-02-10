from collections import defaultdict
import itertools

with open('input') as f:
    input = f.read().splitlines()

pairs = defaultdict(dict)
for line in input:
    name, _, effect, amount, *_, other = line.split(' ')
    pairs[name[0]][other[0]] = int(amount) if effect in 'gain' else int(amount) * -1

# Part 2
guests = list(pairs.keys())
for g in guests:
    pairs['S'][g] = 0
    pairs[g]['S'] = 0
# End part 2

guests = list(pairs.keys())
pair_score = {}
for left, right in itertools.product(guests, guests):
    if left != right: pair_score[left+right] = pairs[left][right] + pairs[right][left]

most = 0
for arrangement in itertools.permutations(guests):
    score = 0
    for i in range(len(arrangement)-1):
        score += pair_score[arrangement[i] + arrangement[i+1]]
    score += pair_score[arrangement[-1] + arrangement[0]]

    if score > most: most = score

print('Answer:', most)