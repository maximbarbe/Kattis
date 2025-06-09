from collections import defaultdict



n, q = map(int, input().split(" "))

solved = defaultdict()
for i in range(1, n+1):
    solved[i] = 0
for i in range(q):
    no, prob = map(int, input().split(" "))
    solved[prob] += 1
print(min(solved.values()))