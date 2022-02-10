with open('input') as f:
    input = f.read().splitlines()

m = 1000
n = 1000

lights = [[0] * m for i in range(n)]

for line in input:
    parts = line.split(' ')
    start = parts[-3].split(',')
    end = parts[-1].split(',')

    start_row = int(start[1])
    start_column = int(start[0])
    end_row = int(end[1])
    end_column = int(end[0])

    if parts[0] == 'toggle':
        l = lambda x: x + 2
    elif parts[1] == 'on':
        l = lambda x: x + 1
    elif parts[1] == 'off':
        l = lambda x: x - 1 if x > 0 else 0

    for i in range(start_row, end_row + 1):
        for j in range(start_column, end_column + 1):
            lights[i][j] = l(lights[i][j])

print(sum(map(sum, lights)))