n, m = map(int, input().split())
res = []
for i in range(1, m+1):
    if i % 3 == 0 or i%5 == 0:
        cur= ""
        if i % 3 == 0:
            cur += "fizz"
        if i % 5 == 0:
            cur += "buzz"
    else:
        cur = str(i)
    res.append(cur)
max_idx = 1
max_count = 0
for i in range(n):
    words = input().split(" ")
    c = 0
    for j in range(len(words)):
        if words[j] == res[j]:
            c += 1
    if c > max_count:
        max_count = c
        max_idx = i + 1
print(max_idx)