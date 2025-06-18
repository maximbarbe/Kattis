mins, n = map(int, input().split(" "))
seconds = mins*60
res = 0
times = [*map(int, input().split(" "))]
times.sort()
for time in times:
    if res + time > seconds:
        break
    else:
        res += time
print(res)