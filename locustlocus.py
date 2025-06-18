from math import floor
n = int(input())
years = []
for i in range(n):
    start, c1, c2 = map(int, input().split())
    s1 = start + c1
    s2 = start + c2
    while s1 != s2:
        if s1 < s2:
            s1 += c1
        else:
            s2 += c2
    years.append(s1)
print(min(years))