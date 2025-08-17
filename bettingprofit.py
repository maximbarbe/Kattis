t = int(input())
for i in range(t):
    m, o, sign = input().split()
    m = int(m)
    o = int(o)
    if sign == "+":
        print(m/100 * o)
    else:
        print(100*m/o)