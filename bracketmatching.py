stack = []
n = int(input())
string = input()

for i in range(len(string)):
    if string[i] in "([{":
        stack.append(string[i])
    else:
        if string[i] == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                print("Invalid")
                exit()
        elif string[i] == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                print("Invalid")
                exit()
        else:
            if len(stack) > 0 and stack[-1] == "{":
                stack.pop()
            else:
                print("Invalid")
                exit()
if len(stack) == 0:
    print("Valid")
else:
    print("Invalid")