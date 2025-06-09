from collections import defaultdict


class Node:
    
    def __init__(self, prev, next, val):
        self.val = val
        self.next = next
        self.prev = prev


class LinkedList:
    
    def __init__(self):
        self.head = Node(prev = None, next = None, val = None)
        self.tail = Node(prev = None, next = None, val = None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.previously_added_node = self.head

    def add_node(self, val):
        to_add = Node(self.previously_added_node, self.previously_added_node.next, val)
        self.previously_added_node.next = to_add
        to_add.next.prev = to_add
        self.previously_added_node = to_add
        return to_add
    
    def print_list(self):
        values = []
        cur = self.head.next
        while cur != self.tail:
            values.append(cur.val)
            cur = cur.next
        return values

    def game(self, sec:Node, first:Node):
        i = 0
        sec_idx = 0
        first_idx = 0
        cur = self.head
        while cur != self.tail:
            if cur == sec:
                sec_idx = i
            if cur == first:
                first_idx = i
            i += 1
            cur = cur.next
        if sec_idx < first_idx:
            return
            
        first.prev.next = first.next
        first.next.prev = first.prev
        first.next = sec.next
        sec.next.prev = first
        sec.next = first
        first.prev = sec

n, m = map(int, input().split(" "))
ll = LinkedList()
nodes = defaultdict()
for i in range(1, n+1):
    nodes[f"T{i}"] = ll.add_node(f"T{i}")
for i in range(m):
    sec, first = input().split(" ")
    ll.game(nodes[sec], nodes[first])
print(" ".join(ll.print_list()))