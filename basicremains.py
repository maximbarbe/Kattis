while n:=input():
    if n == "0":
        exit()
    b, p, m = map(int, n.split())
    p = int(str(p), base=b)
    mod = int(str(m), base=b)
    r = p%mod
    digits = []
    while r != 0:
        digits.append(r%b)
        r //= b
    if digits == []:
        digits.append(0)
    print("".join(map(str, digits[::-1])))