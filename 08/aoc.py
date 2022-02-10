import re

with open('input') as f:
    input = f.read().splitlines()

totalRaw = 0
totalParse = 0

for line in input:
    print(line)
    totalRaw += len(line)
    line = re.escape(line)
    line = line.replace('\"', '\\\"')
    line = '\"' + line + '\"'
    print(line)
    totalParse += len(line)

print(totalParse-totalRaw)