from collections import deque, defaultdict
from functools import lru_cache

@lru_cache
def dfs(cur):
    if ends.get(cur, None) != None:
        if ends[cur] == "favourably":
            return 1
        else:
            return 0
    else:
        res = 0
        for dest in edges[cur]:
            res += dfs(dest)
        return res


t = int(input())
for i in range(t):
    ends = dict()
    edges = defaultdict(lambda:[])
    n = int(input())
    for i in range(n):
        data = input().split()
        page_num = int(data[0])
        if data[1].isnumeric():
            
            for j in range(1, len(data)):
                edges[page_num].append(int(data[j]))
        else:
            ends[page_num] = data[1]
    print(dfs(1))
    dfs.cache_clear()