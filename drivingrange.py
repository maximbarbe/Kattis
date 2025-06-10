class UnionFind:
    # Implemented using the methods described here: https://visualgo.net/en/ufds/print#:~:text=The%20Union%2DFind%20Disjoint%20Sets,sets%20into%20one%20when%20needed.
    # and https://people.cs.georgetown.edu/jthaler/ANLY550/lec6.pdf
    
    def __init__(self, n):
        self.sets = [i for i in range(n)]
        self.rank = [0]*n
        self.num_sets = n

    def find(self, id):
        if self.sets[id] == id:
            return id
        else:
            return self.find(self.sets[id])

    def is_same_set(self, id1, id2):
        return self.find(id1) == self.find(id2)


    def union(self, id1, id2):
        smaller = self.find(id1)
        larger = self.find(id2)
        if (smaller == larger):
            return
        if (self.rank[smaller] > self.rank[larger]):
            smaller, larger = larger, smaller
        elif self.rank[smaller] == self.rank[larger]: self.rank[larger] += 1
        
        self.sets[smaller] = larger
        self.num_sets -= 1
        return True
    
n, m = map(int, input().split())
if m < n - 1:
    print("IMPOSSIBLE")
    exit()
ufds = UnionFind(n)
edges = []
for i in range(m):
    src, dest, weight = map(int, input().split())
    edges.append((src, dest, weight))
edges.sort(key = lambda el: el[2])

for i in range(len(edges)):
    if not ufds.is_same_set(edges[i][0], edges[i][1]):
        ufds.union(edges[i][0], edges[i][1])
    
    
    
    if ufds.num_sets == 1:
        break
if ufds.num_sets != 1:
    print("IMPOSSIBLE")
else:
    print(edges[i][2])