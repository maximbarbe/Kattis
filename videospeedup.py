n, p, k = map(int, input().split(" "))
stamps = [*map(int, input().split(" "))]
lengths = [stamps[0] - 0]
for i in range(len(stamps) - 1):
    lengths.append(stamps[i + 1] - stamps[i])
lengths.append(k - stamps[-1])
res = 0
for i in range(len(lengths)):
    speed = 100 + i*p
    res += lengths[i]/(100/speed)
print(res)