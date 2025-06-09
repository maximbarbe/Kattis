n, diff = map(int, input().split(" "))
notes = []
for i in range(n):
    notes.append(int(input()))
notes.sort()
cur = 0
res = 0
while cur != len(notes):
    minimum = notes[cur]
    for i in range(cur, len(notes)):
        if notes[i] - minimum > diff:
            cur = i
            res += 1
            break
    else:
        res += 1
        break

print(res)