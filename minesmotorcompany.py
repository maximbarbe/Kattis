d = []
for i in range(int(input())):
    d.append(input())
res = 0
for i in range(1, len(d)):
    res += abs(ord(d[i][0]) - ord(d[i - 1][0])) + abs(ord(d[i][1]) - ord(d[i - 1][1]))
print(res)