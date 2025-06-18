from collections import defaultdict
n = int(input())
edges = defaultdict(lambda:set())

def dfs(cur, destination, path, visited, edges):
    if cur == destination:
        print(" ".join(path))
        exit()
    else:
        
        for edge in edges[cur]:
            if edge not in visited:
                temp = visited
                temp.add(edge)
                dfs(edge, destination, path + [edge], temp, edges)


for i in range(n):
    data = input().split(" ")
    for i in range(1, len(data)):
        edges[data[0]].add(data[i])
        edges[data[i]].add(data[0])

src, dest = input().split(" ")
visited = set([src])
dfs(src, dest, [src], visited, edges)
print("no route found")