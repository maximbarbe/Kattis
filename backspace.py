stack = []
string = input()
for i in range(len(string)):
    if string[i] != "<":
        stack.append(string[i])
    else:
        stack.pop(-1)
print("".join(stack))