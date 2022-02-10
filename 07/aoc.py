with open('input') as f:
    input = f.read().splitlines()

mem = dict()


def process(value):
    val = ''

    if value in mem:
        return mem[value]

    if value.isnumeric():
        val = int(value)

    else:
        if 'NOT' in value:
            x = value.split('NOT ')[1]
            val = ~process(wires[x]) + 2**16
        
        else:
            parts = value.split(' ')

            x = parts[0]
            if not x.isnumeric():
                x = wires[x]
            if(len(parts) == 1):
                val = process(x)

            else:
                y = parts[2]
                if not y.isnumeric():
                    y = wires[y]

                if 'AND' in value:
                    val = process(x) & process(y)

                elif 'OR' in value:
                    val = process(x) | process(y)

                elif 'LSHIFT' in value:
                    val = process(x) << int(y)

                elif 'RSHIFT' in value:
                    val = process(x) >> int(y)

    mem[value] = val
    return val


wires = dict()

for line in input:
    parts = line.split(' -> ')
    wires[parts[1]] = parts[0]


print(process(wires['a']))
