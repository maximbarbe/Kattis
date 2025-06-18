from math import floor
while True:
    x = int(input())
    if x == 0:
        break
    symbols = input()
    perm = input()
    encoded = input()
    n = len(encoded)
    res = [None] * n
    d = (floor(n**1.5 + x))%n
    temp = symbols.index(encoded[d])
    res[d] = perm[temp]
    # Start from the letter we found
    # First pass from the letter we found until the front
    # 
    j_1 = d
    j = d-1
    while j != -1:
        second_idx = symbols.index(res[j_1])
        xor_idx = symbols.index(encoded[j])
        for i in range(len(perm)):
            if i ^second_idx == xor_idx:
                break
        res[j] = perm[i]
        j_1 -= 1
        j -=1 
    j_1 = 0
    j = n - 1
    while j != d:
        second_idx = symbols.index(res[j_1])
        xor_idx = symbols.index(encoded[j])
        for i in range(len(perm)):
            if i ^second_idx == xor_idx:
                break
        res[j] = perm[i]
        j_1  = (j_1 - 1)%n
        j -=1 
    print("".join(res))