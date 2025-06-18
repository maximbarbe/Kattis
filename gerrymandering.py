from collections import defaultdict
from math import floor
n, m =map(int, input().split(" "))
dict = defaultdict()
for i in range(1, m+1):
    dict[i] = []
for i in range(n):
    d, votes_a, votes_b = map(int, input().split(" "))
    dict[d].append((votes_a, votes_b))
total_votes = 0
total_wasted_votes_a = 0
total_wasted_votes_b = 0
for key, val in dict.items():
    votes_a = sum([v[0] for v in val])
    votes_b = sum([v[1] for v in val])
    wasted_a = 0
    wasted_b =0
    winner = None
    if votes_a > votes_b:
        winner = "A"
    else:
        winner = "B"
    if winner ==  "A":
        wasted_a = votes_a - (floor((votes_a + votes_b)/2) + 1)
        wasted_b = votes_b
    else:
        wasted_a = votes_a
        wasted_b = votes_b - (floor((votes_a + votes_b)/2) + 1)
    print(f"{winner} {wasted_a} {wasted_b}")
    total_votes += votes_a + votes_b
    total_wasted_votes_a += wasted_a
    total_wasted_votes_b += wasted_b
    
print(abs(total_wasted_votes_a - total_wasted_votes_b)/total_votes)