from collections import defaultdict
import sys

n = 0
winner = None
max_votes = 0
candidates = defaultdict(lambda:0)
for line in sys.stdin:
    line = line.strip("\n")
    if line == "***":
        break
    candidates[line] += 1
    if candidates[line] > max_votes:
        max_votes = candidates[line]
        winner = line
    n += 1

for key, val in candidates.items():
    if val == max_votes and key != winner:
        print("Runoff!")
        exit()
else:
    print(winner)
