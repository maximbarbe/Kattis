problems = input().split(";")
res = 0
for problem in problems:
    if "-" not in problem:
        res += 1
    else:
        i = problem.index("-")
        res += int(problem[i + 1:]) - int(problem[0:i]) + 1
print(res)