from collections import defaultdict

with open('input') as f:
    input = f.read().splitlines()

routes = defaultdict(dict)

for line in input:
    route = line.split(' = ')
    distance = int(route[1])
    city_a = route[0].split(' to ')[0]
    city_b = route[0].split(' to ')[1]
    routes[city_a][city_b] = distance
    routes[city_b][city_a] = distance

distances = []

def eval_route(frm, visited, distance):
    left = [x for x in routes[frm] if x not in visited]

    if len(left) == 0:
        distances.append(distance)

    for r in left:
        eval_route(r, visited + [r], distance + routes[frm][r])

for route in routes:
    eval_route(route, [route], 0)

print(max(distances))