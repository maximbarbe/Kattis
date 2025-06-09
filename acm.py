from collections import defaultdict
import sys

dict = defaultdict(lambda:0)
solved = set()
for line in sys.stdin:
    if line == "-1\n":
        break
    data = line.split(" ")
    if data[-1] == "right\n":
        dict[data[1]] += int(data[0])
        solved.add(data[1])
    else:
        dict[data[1]] += 20
    
    
problems_solved = len(solved)
if problems_solved == 0:
    print("0 0")
else:
    values = 0
    for key in list(solved):
        values += dict[key]
    print(f"{problems_solved} {values}")