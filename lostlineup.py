n = int(input())
if n == 1:
    print(1)
    exit()
lineup = [i for i in range(1, n + 1)]
res = [None for i in range(n)]
res[0] = 1
data = list(map(int, input().split(" ")))
for i in range(2, n+1):
    res[data[i - 2] + 1] = i
print(" ".join(map(str, res)))