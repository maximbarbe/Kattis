n, m = map(int, input().split(" "))
data = [*map(int, input().split(" "))]
for i in range(len(data)):
    if data[i] > n:
        print(len(data) - i)
        break
    else:
        n -= data[i]