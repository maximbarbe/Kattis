times = [0 for i in range(0, 101)]
a, b, c = map(int, input().split(" "))
for i in range(3):
    start, end = map(int, input().split(" "))
    for j in range(start, end):
        times[j] += 1
        
res = 0
for i in range(len(times)):
    if times[i] == 1:
        res +=a
    elif times[i] == 2:
        res += b * 2
    elif times[i] == 3:
        res += c * 3
print(res)