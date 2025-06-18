from collections import Counter
n, m = map(int, input().split())
c = Counter()
for i in range(n):
    c[int(input())] += 1
max_key = 0
max_val = 0
for key, val in c.items():
    if val > max_val:
        max_val = val
        key = key
        
if sum(c.values()) - max_val <= m:
    print("Ja")
else:
    print("Nej")