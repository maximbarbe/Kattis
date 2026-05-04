stack = []


for c in input().split():
    if c in "+-*/":
        o2 = stack.pop()
        o1 = stack.pop()
        stack.append(f'({o1}{c}{o2})')
    else:
        stack.append(c)
print(stack.pop())