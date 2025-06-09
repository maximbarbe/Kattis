n, m = map(int, input().split(" "))
if m >= n:
    print("too late")
    exit()
else:
    ordered = []
    for i in range(m):
        ordered.append(int(input()))
    for i in range(1, n + 1):
        if i not in ordered:
            print(i)
            exit()