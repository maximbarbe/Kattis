from collections import Counter

n, t = map(int, input().split(" "))
A = [*map(int, input().split(" "))]
if t == 1:
    seen = set()
    for i in range(len(A)):
        if A[i] in seen:
            print("Yes")
            exit()
        else:
            seen.add(7777 - A[i])
    else:
        print("No")
        exit()
elif t == 2:
    if len(set(A)) == len(A):
        print("Unique")
    else:
        print("Contains duplicate")
elif t == 3:
    threshold = n/2
    counter = Counter(A)
    for el in counter.keys():
        if counter[el] > threshold:
            print(el)
            exit()
    else:
        print(-1)
elif t == 4:
    A.sort()
    if n % 2 == 1:
        print(A[n // 2 ])
        exit()
    else:
        print(f"{A[n//2 - 1]} {A[n//2]}")
        exit()
else:
    valid = []
    for i in range(len(A)):
        if 100 <= A[i] <= 999:
            valid.append(A[i])
    valid.sort()
    print(" ".join(map(str, valid)))