class LinkedList:
    def __init__(self):
        self.header = Node(None, None, None)
        self.tailer = Node(None, None, None)
        self.header.next = self.tailer
        self.tailer.prev = self.header
        self.cursor = self.header
        
    def add(self, letter):
        to_add = Node(letter, self.cursor.next, self.cursor)
        self.cursor.next.prev = to_add
        self.cursor.next = to_add
        self.cursor = self.cursor.next
        
    def remove(self):
        if self.cursor == self.header:
            return
        else:
            temp = self.cursor.prev
            self.cursor.prev.next = self.cursor.next
            self.cursor.next.prev = self.cursor.prev
            del self.cursor
            
            
            self.cursor = temp    
        
class Node:
    
    def __init__(self, letter, next, prev):
        self.letter = letter
        self.next = next
        self.prev = prev


n = int(input())
for i in range(n):
    words = LinkedList()
    string = input()
    for j in range(len(string)):
        if string[j] == "<":
            words.remove()
        elif string[j] == "]":
            words.cursor = words.tailer.prev
        elif string[j] == "[":
            words.cursor = words.header
        else:
            words.add(string[j])

    cur = words.header.next
    while cur != words.tailer:
        print(cur.letter, end="")
        cur = cur.next
    print()
