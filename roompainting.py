n, m = map(int, input().split(" "))
needed = []
offered = []
for i in range(n):
    offered.append(int(input()))
for i in range(m):
    needed.append(int(input()))
needed.sort()
offered.sort()
needed_idx = 0
offered_idx =0
res = 0
while needed_idx != len(needed) and offered_idx != len(offered):
    if offered[offered_idx] < needed[needed_idx]:
        offered_idx += 1
    else:
        res += offered[offered_idx] - needed[needed_idx]
        needed_idx += 1
        
print(res)