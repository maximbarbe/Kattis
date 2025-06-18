n, m = map(int, input().split())
coords=  []
for i in range(1, n+1):
    row = input()
    for j, char in enumerate(row):
        if char == '*':
           coords.append((i, j + 1))
print(len(coords))
for x, y in coords:
    print(x, y)