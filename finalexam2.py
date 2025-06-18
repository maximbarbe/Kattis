n = int(input())
answers = []
for i in range(n):
    answers.append(input())
res = 0
for i in range(n - 1):
    if answers[i] == answers[i + 1]:
        res += 1
print(res)