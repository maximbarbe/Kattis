from collections import defaultdict, deque


t = int(input())

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []



for i in range(t):
    n = int(input())
    idx = dict()
    roots = []
    for j in range(n):
        p_idx, item = input().split()
        p_idx = int(p_idx)
        new_item = Node(item)
        idx[j] = new_item
        if p_idx != -1:
            idx[p_idx].children.append(new_item)
        else:
            roots.append(new_item)
    levels = defaultdict(lambda:[])
    q = deque([(root, 0) for root in roots])
    while q:
        cur, height = q.popleft()
        levels[height].append(cur.val)
        for c in cur.children:
            q.append((c, height + 1))
    print(" ".join(sorted(levels[max(levels.keys())])))