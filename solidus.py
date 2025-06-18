from math import gcd

first = int(input().strip())
input()
sec = int(input().strip())
if abs(first)%abs(sec)==0:
    print(first//sec)
else:
    g = gcd(abs(first), abs(sec))
    if first < 0 and sec < 0:
        first *= -1
        sec *= -1
    elif sec < 0 and first > 0:
        sec *= -1
        first *= -1
    print(f"{first//g}/{sec//g}")