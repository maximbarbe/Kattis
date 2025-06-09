n = int(input())
present = [0 for i in range(0, n+1)]

while True:
    try:
        a, b = map(int, input().split())
    except EOFError:
        break
    present[a] += 1
    present[b] += 1

first = None
for i in range(1, len(present)):
    if present[i] != 1:
        if first == None:
            first = i
        else:
            print(first, i)
            exit()