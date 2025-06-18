g = int(input())
n = int(input())
cur = 2
for i in range(n):
    a,b = map(int, input().split())
    if cur == a:
        cur = b
    elif cur == b:
        cur = a
if cur == g:
    match cur:
        case 1:
            print(2, 3)
        case 2:
            print(1, 3)
        case 3:
            print(1, 2)
else:
    print(min(g, cur), max(g, cur))