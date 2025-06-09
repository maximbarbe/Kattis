import statistics
from collections import defaultdict
N, t = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
if t == 1:
    print(7)
elif t == 2:
    if A[0] > A[1]:
        print("Bigger")
    elif A[0] == A[1]:
        print("Equal")
    else:
        print("Smaller")
elif t == 3:
    print(statistics.median([A[0], A[1], A[2]]))
elif t == 4:
    print(sum(A))
elif t == 5:
    cur = 0
    for i in range(len(A)):
        if A[i] % 2 == 0:
            cur += A[i]
    print(cur)
elif t == 6:
    for i in range(len(A)):
        A[i] %= 26
        A[i] = chr(ord("a") + A[i])
    print("".join(A))
else:
    visited = defaultdict(lambda: False)
    cur = 0
    while True:
        if visited[cur] == True:
            print("Cyclic")
            break
        elif cur < 0 or cur > len(A) - 1:
            print("Out")
            break
        elif cur == len(A) - 1:
            print("Done")
            break
        else:
            visited[cur] = True
            cur = A[cur]