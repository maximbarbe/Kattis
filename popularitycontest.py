n, m = map(int, input().split(" "))
scores = [-(i) for i in range(1, n + 1)]
for i in range(m):
    first, sec = map(int, input().split(" "))
    scores[first - 1] += 1
    scores[sec - 1] += 1
print(" ".join(map(str, scores)))