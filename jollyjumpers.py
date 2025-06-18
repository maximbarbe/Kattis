import sys
from collections import defaultdict
for line in sys.stdin:
    data = [*map(int, line.split(" "))]
    n = data[0]
    dict = defaultdict(lambda:False)

    if n == 1:
        print("Jolly")
        continue
    else:
        for i in range(1, len(data) - 1):
            dict[abs(data[i] - data[i + 1])] = True
            
    for i in range(1, n):
        if dict[i] == False:
            print("Not Jolly")
            break
    else:
        print("Jolly")