from collections import deque
n = int(input())
x = int(input())
q = deque()
for i in range(n):
    c = input()
    match c:
        case "ADD":
            q.append(i)
        case "PASS":
            continue
        case "EAT":
            while q:
                cur = q.popleft()
                if i - cur <= x:
                    break
            else:
                print("ono..")
                exit()
else:
    print("yay!")