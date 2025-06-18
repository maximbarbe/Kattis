from functools import lru_cache

# Recursive formula found here: https://oeis.org/A006046
@lru_cache(0)
def recur(n):
    if n in [0, 1]:
        return n
    else:
        if n % 2 == 0:
            return 3*recur(n//2)
        else:
            temp = (n-1)//2
            return 2*recur(temp) + recur(temp + 1)
n = int(input())
print(recur(n))