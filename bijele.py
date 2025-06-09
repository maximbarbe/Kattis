pieces = [1, 1, 2, 2, 2, 8]
current = list(map(lambda x: int(x), input().split(" ")))
for i in range(len(current)):
    current[i] = str(pieces[i] - current[i])
print(" ".join(current))