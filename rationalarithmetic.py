from math import gcd
n = int(input())
for i in range(n):
    x1, y1, op, x2, y2 = input().split()
    x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])

    if op == "+":
        
        denom = y1 *y2
        num = y2* x1 + x2*y1
        
        
    elif op == "-":
        denom = y1 *y2
        num = y2* x1 - x2*y1
        
        
    elif op == "/":
        num = x1 * y2
        denom = x2 * y1
        
    else:
        num = x1 * x2
        denom = y1*y2
    if num > 0 and denom < 0 or num < 0 and denom < 0:
        num = -num
        denom = -denom
    temp = gcd(num, denom)
    print(f"{num//temp} / {denom//temp}")