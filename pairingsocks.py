from collections import defaultdict
n = int(input())




vals = defaultdict(lambda:0)
stack = [*map(int, input().split(" "))][::-1]
aux = []

for i in range(len(stack)):
    vals[stack[i]] += 1
    
for val in vals.values():
    if val % 2 == 1:
        print("impossible")
        exit()
    
moves = 0
while True:
    if aux == []:
        aux.append(stack.pop())
        moves += 1
    else:
        if aux[-1] == stack[-1]:
            aux.pop()
            stack.pop()
            moves += 1
        else:
            aux.append(stack.pop())
            moves += 1 
    if aux == [] and stack == []:
        break
    if stack == []:
        print("impossible")
        exit()

print(moves)