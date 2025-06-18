from collections import defaultdict


def is_enough(curNode, amt):
    if values[curNode - 1] != -1:
        if values[curNode - 1] <= amt:
            return True
        else:
            return False
    res = True
    for node in edges[curNode]:
        if edges[curNode][node][1]== 1:
            res = res and is_enough(node, (amt * edges[curNode][node][0]) ** 2)
        else:
            res = res and is_enough(node, (amt * edges[curNode][node][0]))
    return res

edges = defaultdict(lambda : None)
n = int(input())
for i in range(n - 1):
    a,b,x,t = map(int, input().split())
    if edges[a] == None:
        edges[a] = defaultdict(lambda:None)
    
    edges[a][b] = (x/100,t)
    
values = [*map(int, input().split())]


l, r = 0, 100000000
while abs(l-r) > 0.0001:
    m = l + (r-l)/2
    if is_enough(1, m):
        r = m
    else:
        l = m
print(l)