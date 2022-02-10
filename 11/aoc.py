with open('input') as f:
    input = f.read()

def following(char):
    return chr(ord(char) + 1)

def next_char(char):
    next = {'z': 'a', 'h': 'j', 'n': 'p', 'k': 'm'}
    if char in next:
        return next[char]
    else:
        return following(char)

def straight(password):
    for c in password:
        if c + following(c) + following(following(c)) in password:
            return True

    return False 

def pair(password):
    first = ''

    for c in password:
        if first == '' and c + c in password:
            first = c
        
        elif first != c and c + c in password:
            return True

    return False 

def valid(password):
    return pair(password) and straight(password)

def next_password(password):
    first = True
    while first or not valid(password):
        first = False
        reverse = list(password[::-1])
        
        for i in range(len(reverse)):
            new_c = next_char(reverse[i])
            reverse[i] = new_c
            if new_c != 'a': break

        password = "".join(reverse[::-1])

    return password

print(next_password(input))