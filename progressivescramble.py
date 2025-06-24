


values = {
    " ": 0,
}

for i in range(26):
    values[chr(ord('a') + i)] = i + 1

reverse = {val:key for key, val in values.items()}

def encode(s):
    vsi = [values[c] for c in s]
    for i in range(1, len(vsi)):
        vsi[i] = vsi[i] + vsi[i - 1]
    for i in range(1, len(vsi)):
        vsi[i] %= 27
    return "".join(map(lambda el:reverse[el], vsi))


def decode(s):
    vsi = [values[c] for c in s]
    sum = 0
    for i in range(1, len(vsi)):
        if vsi[i] > vsi[i - 1]:
            continue
        else:
            while vsi[i] < vsi[i - 1]:
                vsi[i] += 27
    sum = vsi[0]
    for i in range(1, len(s)):
        vsi[i] -= sum
        sum += vsi[i]
    return "".join(map(lambda el:reverse[el], vsi))


n = int(input())
for i in range(n):
    line = input()
    c = line[0]
    s = line[2:]
    if c == "e":
        print(encode(s))
    else:
        print(decode(s))
    
    