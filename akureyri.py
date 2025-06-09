from collections import defaultdict

pos = defaultdict(lambda:0)
n = int(input())
for i in range(n):
    name,loc = input(),input()
    pos[loc] += 1
values = [(key, val) for key, val in pos.items()]
values.sort(key=lambda el:(el[1],el[0]))
for key, val in values:
    print(key, val)