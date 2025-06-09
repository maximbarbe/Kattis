from math import dist
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
    

t = int(input())
for i in range(t):
    s, p = map(int, input().split())
    ufds = UnionFind(p)
    
    # (src, dest, weight)
    edges = []
    
    # (x, y, id)
    points = []
    
    for i in range(p):
        x, y = map(int, input().split())
        for j in range(len(points)):
            edges.append((i, j, dist((x, y), (points[j][0], points[j][1]))))
            
        points.append((x, y, i))
    edges.sort(key = lambda el: el[2])
    taken = []
    while ufds.num_sets != s:
        cur = edges.pop(0)
        if not ufds.is_same_set(cur[0], cur[1]):
            ufds.union(cur[0], cur[1])
            taken.append(cur[2])
    print(f"{max(taken):.2f}")