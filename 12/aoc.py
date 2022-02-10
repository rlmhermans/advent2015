import json

with open('input') as f:
    input = f.read()

def sum(d):
    count = 0
    t = str(type(d))    

    if 'dict' in t:
        for x in d:
            if 'red' == d[x]:
                return 0 
        
    if 'int' in t:
        count += d
    else:
        for x in d:
            if 'list' in t:
                count += sum(x)
            elif 'dict' in t:
                count += sum(d[x])

    return count 

j = json.loads(input)

print(sum(j))