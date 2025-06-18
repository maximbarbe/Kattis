n, lph = map(int, input().split(" "))
total = 5 * lph
diff = []
for i in range(n):
    diff.append(int(input()))
diff.sort()
res = 0
for i in range(len(diff)):
    if diff[i] <= total:
        total -= diff[i]
        res += 1
    else:
        break
print(res)