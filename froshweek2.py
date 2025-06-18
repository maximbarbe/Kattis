n, m = map(int, input().split())

task_times = sorted([*map(int, input().split())], reverse=True)
quiet_times = sorted([*map(int, input().split())], reverse=True)

res = 0

t_idx = 0
q_idx = 0
while t_idx != len(task_times) and q_idx != len(quiet_times):
    if task_times[t_idx] > quiet_times[q_idx]:
        t_idx += 1
    else:
        res += 1
        t_idx += 1
        q_idx += 1
print(res)