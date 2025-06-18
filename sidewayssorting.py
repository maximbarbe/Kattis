first = True

while True:
    r, c = map(int, input().split(" "))
    if r == 0 and c == 0:
        break
    if not first:
        print()
    first = False
    grid = []
    words_to_sort = []
    for i in range(r):
        grid.append(input())
    for i in range(c):
        cur = ""
        for j in range(r):
            cur += grid[j][i]
        words_to_sort.append(cur)
    words_to_sort.sort(key = lambda el:(el.lower()))
    for i in range(r):
        for j in range(c):
            print(words_to_sort[j][i], end="")
        print()