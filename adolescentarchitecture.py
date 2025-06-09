from math import sqrt
n = int(input())
res = []
for i in range(n):
    type, l1 = input().split()
    l2 = None
    l1 = int(l1)
    l2 = l1
    if type == "cylinder":
        l1 = l1*sqrt(2)
    res.append((type, l1, l2))
    
res.sort(key=lambda el: el[1], reverse=True)
for i in range(1, len(res)):
    if res[i][0] == 'cylinder':
        if res[i - 1][0] == 'cube':
            if 2*res[i][2] > res[i - 1][1]:
                print("impossible")
                exit()
    elif res[i][0] == 'cube':
        if res[i - 1][0] == 'cylinder':
            if res[i][1] > 2*res[i - 1][2]:
                print("impossible")
                exit()
for i in range(len(res) -1, -1, -1):
    print(res[i][0], res[i][2])