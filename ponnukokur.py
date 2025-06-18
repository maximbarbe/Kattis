class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def build_tree(values, l, r):
        if l == r:
            node = Node(values[l])
            return node
        else:
            node = Node(0)
            node.left = Node.build_tree(values, l, (l+r)//2)
            node.right = Node.build_tree(values, (l + r)//2 + 1, r)
            if node.left:
                node.value += node.left.value
            if node.right:
                node.value += node.right.value
            return node
        
    def update(root, pos, l, r):
        if l == r:
            root.value ^= 1
            return
        else:
            if l <= pos <= (l + r)//2:
                Node.update(root.left, pos, l, (l+r)//2)
            else:
                Node.update(root.right, pos, (l+r)//2 + 1, r)
            root.value = 0
            if root.left:
                root.value += root.left.value
            if root.right:
                root.value += root.right.value
            return
    def range_sum(root, a, b, l, r):
        if a == l and b == r:
            return root.value
        else:
            mid = (l + r)//2
            if b <= mid:
                return Node.range_sum(root.left, a, b, l, mid)
            elif a >= mid + 1:
                return Node.range_sum(root.right, a, b, mid + 1, r)
            else:
                return Node.range_sum(root.left, a, mid, l, mid) + Node.range_sum(root.right, mid+1, b, mid + 1, r)
        
n, q = map(int, input().split())
pancakes = Node.build_tree([0]*n, 0, n-1)
flipped = False
for i in range(q):
    data = [*map(int, input().split())]
    match data[0]:
        case 1:
            Node.update(pancakes, data[1] - 1, 0, n-1)
        case 2:
            flipped ^= True
        case 3:
            res = Node.range_sum(pancakes, 0, n-1, 0, n-1)
            if flipped:
                print(n-res)
            else:
                print(res)
        case 4:
            l = data[1] - 1
            r = data[2]  - 1
            l = max(l, 0)
            r = min(r, n-1)
            res = Node.range_sum(pancakes, l, r, 0, n-1)
            if flipped:
                print(r-l + 1-res)
            else:
                print(res)