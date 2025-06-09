from math import inf, dist
import heapq



class Node:
    def __init__(self, name, partner = None, next = None, prev = None):
        self.name = name
        self.partner = partner
        self.next = next
        self.prev = prev
        
        
class LinkedList:
    
    def __init__(self):
        self.header = Node(None, None)
        self.trailer = Node(None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.mic_holder = None
        self.size = 0
    def add_node_to_list(self, node):
        if self.size == 1:
            self.mic_holder = self.header.next
        
        temp = self.trailer.prev
        self.trailer.prev = node
        node.prev = temp
        temp.next = node
        node.next = self.trailer
        self.size += 1
        
    def f_command(self):
        self.mic_holder = self.mic_holder.prev
        
    def b_command(self):
        self.mic_holder = self.mic_holder.next
        
    def r_command(self):
        if self.mic_holder.next == self.trailer:
            self.mic_holder = self.header.next
        else:
            temp = self.mic_holder
            self.mic_holder = self.mic_holder.next
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            self.add_node_to_list(temp)
            
    def c_command(self):
        temp = self.mic_holder
        if self.mic_holder.next == self.trailer:
            self.mic_holder = self.header.next
        else:
            self.mic_holder = self.mic_holder.next
        node_to_add_after = temp.partner
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        
        temp2 = node_to_add_after.next
        node_to_add_after.next = temp
        temp.next = temp2
        temp2.prev = temp
        temp.prev = node_to_add_after
        
            
        
    def p_command(self):
        print(self.mic_holder.partner.name)
        
n,q = map(int, input().split())
ll = LinkedList()
for i in range(n):
    name1, name2 = input().split()
    node1 = Node(name1)
    node2 = Node(name2)
    node1.partner = node2
    node2.partner = node1
    ll.add_node_to_list(node1)
    ll.add_node_to_list(node2)
commands = input()
for char in commands:
    match char:
        case "P":
            ll.p_command()
        case "B":
            ll.b_command()
        case "F":
            ll.f_command()
        case "R":
            ll.r_command()
        case _:
            ll.c_command()
print()
cur = ll.header.next
while cur != ll.trailer:
    print(cur.name)
    cur = cur.next