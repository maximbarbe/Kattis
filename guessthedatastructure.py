import sys
from collections import deque
import heapq
first = True

for line in sys.stdin:
    data = [*map(int, line.strip("\n").split(" "))]
    if len(data) == 1:
        if first == False:
            if impossible or not stack and not queue and not p_queue:
                print("impossible")
            elif stack and queue:
                print("not sure")
            elif stack and p_queue:
                print("not sure")
            elif queue and p_queue:
                print("not sure")
            elif stack:
                print("stack")
            elif queue:
                print("queue")
            elif p_queue:
                print("priority queue")
            
        first = False
        stack = True
        queue = True
        p_queue = True
        impossible = False
        st = []
        heap = []
        q = deque()
        
    else:
        if data[0] == 1:
            st.append(data[1])
            q.append(data[1])
            heapq.heappush(heap, -data[1])
        else:
            if data[1] not in st:
                impossible = True
                stack = False
                queue = False
                p_queue = False
                continue
            if stack and data[1] == st[-1]:
                st.pop(-1)
            else:
                stack = False
            if queue and data[1] == q.popleft():
                pass
            else:
                queue = False
            if p_queue and -data[1] == heap[0]:
                heapq.heappop(heap)
            else:
                p_queue = False
        
else:
    if impossible or not stack and not queue and not p_queue:
        print("impossible")
    elif stack and queue:
        print("not sure")
    elif stack and p_queue:
        print("not sure")
    elif queue and p_queue:
        print("not sure")
    elif stack:
        print("stack")
    elif queue:
        print("queue")
    elif p_queue:
        print("priority queue")