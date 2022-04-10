with open('input') as f:
    input = f.read().splitlines()

correct_sue = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3,
               'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

sues = {}
sue = 1
for line in input:
    attributes = {}
    line = line.split(': ', 1)[1]
    for attribute in line.split(', '):
        k, v = attribute.split(': ')
        attributes[k] = int(v)
    sues[sue] = attributes
    sue += 1

for number, attr in sues.items():
    correct = True

    for cat, amount in attr.items():
        if cat in correct_sue:
            if 'cats' in cat or 'tree' in cat:
                if not correct_sue[cat] < amount:
                    correct = False

            elif 'pomeranians' in cat or 'goldfish' in cat:
                if not correct_sue[cat] > amount:
                    correct = False

            elif not correct_sue[cat] == amount:
                correct = False

    if correct:
        print('Part 1:', number)
