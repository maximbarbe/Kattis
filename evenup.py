n = int(input())
stack = []
vals = [*map(int, input().split())]
for i in range(n):
    if stack == []:
        stack.append(vals[i])
    else:
        if (stack[-1] + vals[i])%2 == 0:
            stack.pop()
        else:
            stack.append(vals[i])
print(len(stack))