r, c = map(int, input().split(" "))
rows = [*map(int, input().split(" "))]
cols = [*map(int, input().split(" "))]

if max(rows) <= max(cols) and max(cols) <= max(rows):
    print("possible")
else:
    print("impossible")