p = int(input())
n = int(input())
problems = input().split()
scores = [0] * p
for i in range(n):
    s=[*map(int, input().split())]
    for j in range(len(s)):
        scores[j] += s[j]
max_score = 0
idx = 0
for i in range(len(scores)):
    if scores[i] > max_score:
        idx = i
        max_score = scores[i]
print(problems[idx])