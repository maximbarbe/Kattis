import sys
from math import inf
for line in sys.stdin:
    data = [*map(int, line.strip("\n").split(" "))]
    if len(data) == 1:
        if data[0] == 0:
            break
        else:
            max_width = data[0]
            pieces = []
            cur = (0, 0)
    else:
        if data[0] == data[1] == -1:
            pieces.append(cur)
            print(f"{max(pieces, key=lambda el:el[0])[0]} x {sum(pieces[j][1] for j in range(len(pieces)))}")
        else:
            if cur[0] + data[0] <= max_width:
                cur = (cur[0] + data[0], max(data[1], cur[1]))
            else:
                pieces.append(cur)
                cur = (data[0], data[1])