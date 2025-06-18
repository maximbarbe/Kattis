n = int(input())
res = [i for i in range(1, n+1)]
rip = False
while len(res) != 1:
    next = []
    for i in range(len(res)):
        if not rip:
            next.append(res[i])
        rip ^= True
    res = next
print(res[-1])