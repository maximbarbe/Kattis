
def t_i(A, B, C, prev):
    
    return ((A*prev + B)%C) + 1

mod = 1_000_000_007
num, length = map(int, input().split(" "))

A, B, C, prev_problem = map(int, input().split(" "))

problems = [prev_problem] + [0 for i in range(num-1)]
for i in range(1, len(problems)):
    problems[i] = t_i(A, B, C, problems[i - 1])
problems.sort()
penalty = 0
time_from_start = 0
res = 0
for i in range(len(problems)):
    if problems[i] + time_from_start > length:
        break
    else:
        time_from_start += problems[i]
        penalty += time_from_start
        res += 1
print(f"{res} {penalty%mod}")