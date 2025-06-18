n = int(input())
for i in range(n):
    P, R, F = map(int, input().split(" "))

    count = 0
    while P <= F:
        P *= R
        count += 1
    print(count)