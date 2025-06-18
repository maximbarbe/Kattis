n = int(input())
times = []
for i in range(n):
    m, o = map(int, input().split())
    times.append((m, o))
times.sort(key=lambda el:el[0])
for t, o in times:
    if o == 0:
        print(t)
        exit()
else:
    print(-1)