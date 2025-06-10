from itertools import combinations
from collections import defaultdict

n, k = map(int, input().split())
problems = []
for i in range(n):
    data = input().split()
    problems.append(data[1:])
    
res = 0
for comb in combinations(problems, k):
    subjects = defaultdict(lambda:0)
    for prob in comb:
        for subject in prob:
            subjects[subject] += 1
    limit = k //2
    for val in subjects.values():
        if val > limit:
            break
    else:
        res += 1
print(res)