from collections import deque
import sys

class Teque:
    def __init__(self):
        self.front = deque()
        self.back = deque()
        
        
    def push_back(self, x):
        self.back.append(x)
        self._rebalance()
    
    def push_front(self, x):
        self.front.appendleft(x)
        self._rebalance()
    
    def push_middle(self, x):
        self.back.appendleft(x)
        self._rebalance()
    
    def _rebalance(self):
        if len(self.front) == len(self.back) or len(self.front) - 1 == len(self.back):
            return
        elif len(self.back) > len(self.front):
            while len(self.back) > len(self.front):
                self.front.append(self.back.popleft())
            return
        elif len(self.front) == len(self.back) + 2:
            self.back.appendleft(self.front.pop())
            return
        
    def get(self, i):
        if len(self.front) <= i:
            return self.back[i - len(self.front)]
        else:
            return self.front[i]

teque = Teque()
for j, line in enumerate(sys.stdin):
    if j == 0:
        continue
    c, v = map(lambda el:el.rstrip(), line.split(" "))
    match c:
        case "push_back":
            teque.push_back(v)
        case "push_front":
            teque.push_front(v)
        case "push_middle":
            teque.push_middle(v)
        case "get":
            sys.stdout.write(teque.get(int(v)) +"\n")