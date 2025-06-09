times = [0 for i in range(1001)]
n = int(input())
for i in range(n):
    start, end = map(int, input().split(" "))
    for j in range(start, end+1):
        times[j] += 1
for i in range(len(times)):
    if times[i] == n:
        print("gunilla has a point")
        exit()
else:
    print("edward is right")