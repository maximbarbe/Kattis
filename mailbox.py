from functools import lru_cache
import sys
from math import inf

# Memoized recursion
@lru_cache(maxsize=None)
def find(mailboxes, upper_bound, lower_bound):
    if lower_bound > upper_bound:
        return 0
    if mailboxes == 1:
        return (upper_bound*(upper_bound + 1))//2 - (lower_bound*(lower_bound - 1))//2
    cur = inf
    for i in range(lower_bound, upper_bound + 1):
        cur =min(cur, i + max(find(mailboxes -1, i - 1, lower_bound), find(mailboxes, upper_bound, i + 1)))
    return cur
n = int(input())
for i in range(n):
    k, n = map(int, input().split())
    print(find(k, n, 1))