from collections import defaultdict

class UnionFind:
    # Implemented using the methods described here: https://visualgo.net/en/ufds/print#:~:text=The%20Union%2DFind%20Disjoint%20Sets,sets%20into%20one%20when%20needed.
    # and https://people.cs.georgetown.edu/jthaler/ANLY550/lec6.pdf
    
    def __init__(self):
        self.sets = defaultdict(lambda:None)
        self.set_sizes = defaultdict(lambda:1)
        

    def find(self, name):
        if self.sets[name] == name:
            return name
        else:
            return self.find(self.sets[name])


    def exists(self, name):
        if self.sets[name] == None:
            return False
        else:
            return True

    def is_same_set(self, id1, id2):
        return self.find(id1) == self.find(id2)


    def union(self, id1, id2):
        if not self.exists(id1):
            self.sets[id1] = id1
            self.set_sizes[id1] = 1
        if not self.exists(id2):
            self.sets[id2] = id2
            self.set_sizes[id2] = 1
        smaller = self.find(id1)
        larger = self.find(id2)
        if self.set_sizes[smaller] > self.set_sizes[larger]:
            smaller, larger = larger, smaller
        if (smaller == larger):
            return
        
        
        self.set_sizes[larger] += self.set_sizes[smaller]
        self.set_sizes[smaller] = self.set_sizes[larger]
        self.sets[smaller] = larger

        return True
    
n = int(input())
ufds = UnionFind()
for i in range(n):
    v1, v2 = input().split()
    ufds.union(v1, v2)
    print(ufds.set_sizes[ufds.find(v1)])