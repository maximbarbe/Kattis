c, k, m = map(int, input().split(" "))
solutions = []
for x in range(0, c + 1):
    y = (c - k*x)//m
    if k*x + m*y == c and x >= 0 and y >= 0:
        solutions.append((x, y))
if len(solutions) == 0:
    print("Impossible")
else:
    el = min(solutions, key=lambda el:el[0] + el[1])
    print(f"{el[0]} {el[1]}")