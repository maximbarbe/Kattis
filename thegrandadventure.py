n = int(input())
for i in range(n):
    stack = []
    string = input()
    ended = False
    for j in range(len(string)):
        if string[j] in "$|*":
            stack.append(string[j])
        elif string[j] == "t":
            while stack != [] and stack[-1] != "|":
                stack.pop()
            if len(stack) == 0:
                ended = True
                print("NO")
                break
            else:
                stack.pop()
        elif string[j] == "j":
            while stack != [] and stack[-1] != "*":
                stack.pop()
            if len(stack) == 0:
                ended = True
                print("NO")
                break
            else:
                stack.pop()      
        elif string[j] == "b":
            while stack != [] and stack[-1] != "$":
                stack.pop()
            if len(stack) == 0:
                ended = True
                print("NO")
                break
            else:
                stack.pop()
    if not ended:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")