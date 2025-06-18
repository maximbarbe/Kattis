s, p = map(int, input().split())
p /= 100
cur = 0
max_res = 0
seen = set()
while True:
    if cur in seen:
        break
    seen.add(cur)
    cur += s
    max_res = max(max_res, cur)
    cur -= cur*p
print(max_res)