from collections import deque

left = deque()
right = deque()
string = input()
for char in string:
    match char:
        case "L":
            right.appendleft(left.pop())
        case "R":
            left.append(right.popleft())
        case "B":
            left.pop()
        case _:
            left.append(char)
print("".join(left) + "".join(right))