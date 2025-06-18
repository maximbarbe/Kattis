from collections import deque

t = int(input())
for i in range(t):
    command = input()
    n = int(input())
    values = input().strip("[]").split(",")
    reverse = False
    error = False
    if values == ['']:
        vals = []
    else:
        vals = deque([*map(int, values)])
    for char in command:
        match char:
            case "R":
                reverse ^= True
                
            case _:
                if len(vals) == 0:
                    error = True
                else:
                    if not reverse:
                        vals.popleft()
                    else:
                        vals.pop()

        if error:
            print("error")
            break
    else:
        print(f"[{','.join(map(str, reversed(vals) if reverse == True else vals))}]")