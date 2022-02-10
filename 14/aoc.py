import math
from collections import defaultdict

with open('input') as f:
    input = f.read().splitlines()

seconds = 2503
reindeer = []
for line in input:
    name, _, _, speed, _, _, duration, *_, rest, _ = line.split(' ')
    reindeer.append((name,int(speed), int(duration), int(rest)))

points = defaultdict(int)
for second in range(1, seconds + 1):
    distances = {}
    for name, speed, duration, rest in reindeer:
        cycle = duration + rest
        cycle_distance = speed * duration
        whole = math.floor(second / cycle)
        part = second % cycle
        distance = whole * cycle_distance + min(part * speed, cycle_distance)
        distances[name] = distance

    most = max(distances.values())
    for k, v in distances.items():
        if v == most: points[k] += 1

print('Answer:', points)