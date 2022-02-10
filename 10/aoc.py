with open('input') as f:
    input = f.read()

def look_and_say(input):
    current = 0
    count = 0
    result = ''

    for i in range(len(input)):
        c = int(input[i])

        if current != c:
            if current != 0: result += f'{count}{current}'
            current = c
            count = 0

        count += 1

    result += f'{count}{current}'
    
    return result

for _ in range(50):
    input = look_and_say(input)

print(len(input))