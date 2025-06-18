res = []
n = int(input())
me = list(map(int, input().split(" ")))
col_1 = list(map(int, input().split(" ")))
col_2 = list(map(int, input().split(" ")))
for i in range(n):
    a = me[i]
    b = col_1[i]
    c = col_2[i]
    res.append(str(sorted([a, b, c])[1]))
print(" ".join(res))