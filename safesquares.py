cols = [False]*8
rows = [False]*8
for i in range(8):
    row = input()
    for j in range(8):
        if row[j] == 'R':
            cols[j] = True
            rows[i] = True
res = 0 
for i in range(8):
    for j in range(8):
        if not cols[j] and not rows[i]:
            res += 1
print(res)