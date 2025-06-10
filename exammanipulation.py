from itertools import product
n, k = map(int, input().split())
scores = []
for i in range(n):
    scores.append(input())
scores = list(set(scores))
min_score = 0
for el in product(["T", "F"], repeat=k):
    m = 10**9
    for score in scores:
        cur = 0
        for i in range(k):
            if score[i] == el[i]:
                cur += 1
        m = min(cur, m)
    min_score = max(min_score, m)
print(min_score)