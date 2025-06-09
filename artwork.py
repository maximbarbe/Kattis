from collections import defaultdict, deque
import sys
from functools import lru_cache

class UFDS:
    
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.degrees = [1 for i in range(n)]
        self.num_sets = 0
    
    
    def get_parent(self, idx):
        if self.parents[idx] == idx:
            return idx
        self.parents[idx] = self.get_parent(self.parents[idx])
        return self.parents[idx]
    
    def is_same_set(self, idx1, idx2):
        return self.get_parent(idx1) == self.get_parent(idx2)

    def size(self, idx):
        return self.degrees[idx]
    
    def merge(self, idx1, idx2):
        
        parent1 = self.get_parent(idx1)
        parent2 = self.get_parent(idx2)
        
        if parent1 == parent2:
            return
        else:
            self.num_sets -= 1
            if self.degrees[parent1] > self.degrees[parent2]:
                self.parents[parent1] = parent2
                self.degrees[parent2] += self.degrees[parent1]
            else:
                self.parents[parent2] = parent1
                self.degrees[parent1] += self.degrees[parent2]

visited = defaultdict(lambda: False)
n,m,q = map(int, input().split())
grid = [[True for i in range(n)] for j in range(m)]
added = defaultdict(lambda:False)
queries = []
c = 0
for i in range(q):
    cur = set()
    x1, y1, x2, y2 = map(lambda el:int(el) - 1, input().split())
    queries.append(cur)
    if x1 == x2:
        for i in range(y1, y2 + 1):
            if grid[i][x1] == True:    
                grid[i][x1] = False
                cur.add((i, x1))

    else:
        for i in range(x1, x2 + 1):
            if grid[y1][i] == True:
                grid[y1][i] = False
                cur.add((y1, i))

            
ufds = UFDS(n*m)

for i in range(m):
    for j in range(n):
        if grid[i][j]:
            ufds.num_sets += 1
            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= i + x < m and 0 <= j + y < n and grid[i + x][y+j]:
                    ufds.merge(i*n + j, (i +x)*n+j+y)
                                
res = []                    
for cur in queries[::-1]:
    res.append(ufds.num_sets)
    for i, j in cur:
        if not grid[i][j]:
            ufds.num_sets += 1
            grid[i][j] = True
            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= i + x < m and 0 <= j + y < n and grid[i + x][j + y]:
                    ufds.merge(i*n + j, (i +x)*n+j+y)

for r in res[::-1]:
    print(r)