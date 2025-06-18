n = int(input())

minimum = n
ids = []
for i in range(n):
    ids.append(int(input()))

while True:
    seen = set()
    for i in range(len(ids)):
        cur = ids[i] % minimum
        if cur in seen:
            break
        seen.add(cur)
    else:
        print(minimum)
        exit()
    minimum += 1