from typing import Dict, List

wants = dict()
has = dict()
names = dict()
visited = dict()
n = int(input())

def dfs(visited:Dict, path:List, wants:Dict, has:Dict, names:Dict, cur:str):
    if wants.get(names[cur][0], None) == None:
        return 0
    else:
        visited[cur] = True
        if wants.get(names[cur][0], None) in path:
            path.append(cur)
            return len(path) - path.index(wants.get(names[cur][0], None))
        else:
            path.append(cur)
            return dfs(visited, path, wants, has, names, wants.get(names[cur][0], None))


for i in range(n):
    name, h, w = input().split()
    wants[w] = name
    has[h] = name
    names[name] = (h, w)
    visited[name] = False

res = 0
for name in names.keys():
    if visited[name] == False:
        res = max(dfs(visited, [], wants, has, names, name), res)
print("No trades possible" if res == 0 else res)