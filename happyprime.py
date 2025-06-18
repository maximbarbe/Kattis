# miller rabin prime test

def is_prime(n):
    temp = n- 1
    s, d = 0, 0
    while temp % 2 == 0:
        s += 1
        temp //= 2
    d = temp

    vals = [2, 3]
    if n in vals:
        return True
    for a in vals:
        x = pow(a, d, n)
        for i in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != n -1:
                return False
            x = y
        if y != 1:
            return False
    return True

def is_happy(num, seen):
    if num in seen:
        return False
    if num == 1:
        return True
    seen.add(num)
    digit = [int(char) for char in str(num)]
    res = 0
    for i in range(len(digit)):
        res += digit[i] ** 2
    return is_happy(res, seen)


n = int(input())
for i in range(n):
    k, m =map(int, input().split(" "))
    if m == 1 or (m % 2 == 0 and m!=2):
        print(f"{k} {m} NO")
    elif not is_prime(m) or not is_happy(m, set()):
        print(f"{k} {m} NO")
    else:
        print(f"{k} {m} YES")