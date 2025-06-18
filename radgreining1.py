n, m = map(int, input().split(" "))
sequence = [None for i in range(n)]
for i in range(m):
    start, seq = input().split(" ")
    start = int(start) - 1
    for j in range(len(seq)):
        if sequence[start + j] == None:
            sequence[start + j] = seq[j]
        else:
            if sequence[start + j] != seq[j]:
                print("Villa")
                exit()
            else:
                continue
for i in range(len(sequence)):
    if sequence[i] == None:
        sequence[i] = "?"
print("".join(sequence))