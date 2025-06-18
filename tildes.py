class Node:
    def __init__(self, id):
        self.id = id
        self.rep = self
        self.size = 1


class UnionFind:
    # Implemented using the pseudo-code shown in this vid: https://www.youtube.com/watch?v=axaOsCgpupk&t=641s&ab_channel=AlgorithmswithAttitude

    
    def __init__(self):
        self.sets = []
        
    def make_set(self, id):
        self.sets.append(Node(id))

    def find(self, id):
        if self.sets[id].rep == self.sets[id]:
            return self.sets[id]
        return self.find(self.sets[id].rep.id)

    def union(self, id1, id2):
        smaller = self.find(id1)
        larger = self.find(id2)
        if (smaller == larger):
            return
        if (smaller.size > larger.size):
            smaller, larger = larger, smaller
        smaller.rep = larger.rep
        larger.size += smaller.size
        return True
    

ufds = UnionFind()
n, m = map(int, input().split(" "))
for i in range(n):
    ufds.make_set(i)

for i in range(m):
    data = input().split()
    if data[0] == "t":
        ufds.union(int(data[1]) - 1, int(data[2]) - 1)
    else:
        idx = int(data[1]) - 1
        print(ufds.find(idx).size)