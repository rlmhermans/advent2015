from itertools import combinations

input = []
with open('input') as f:
    for n in f.read().splitlines():
        input.append(int(n))

comb = []
for i in range(len(input) + 1):
    comb += list(combinations(input, i))

adds = [len(c) for c in comb if sum(list(c)) == 150]
min_cont = min(adds)
adds = [c for c in comb if sum(list(c)) == 150 and len(c) ==  min_cont]

print(len(adds))