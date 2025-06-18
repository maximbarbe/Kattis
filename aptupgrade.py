n, m, k = map(int, input().split())
v = sorted([*map(int, input().split())], reverse=True)
total = sum(v)
downloaded = 0
for i in range(min(n, m + k)):
    downloaded += v[i]
print((downloaded/total)*100)