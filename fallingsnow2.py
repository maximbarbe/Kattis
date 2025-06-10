n, m = map(int, input().split())
cols = {i:0 for i in range(m)}
for i in range(n):
    row = input()
    for j in range(m):
        if row[j] == "S":
            cols[j] += 1
for i in range(n):
    for j in range(m):
        if i >= n - cols[j]:
            print("S", end="")
        else:
            print(".", end="")
    print()