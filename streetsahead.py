n, m = map(int, input().split())

nmb = dict()
for i in range(n):
    nmb[input()] = i
for i in range(m):
    start, end = input().split()
    if nmb[start] > nmb[end]:
        start, end = end, start
    print(nmb[end] - nmb[start] - 1)