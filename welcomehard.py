from functools import lru_cache
import sys

to_find = 'welcome to code jam'

@lru_cache(sys.maxsize)
def backtrack(idx, i, word):
    
    if i == len(to_find):
        return 1
    if idx == len(word):
        return 0
    else:
        if word[idx] == to_find[i]:
            return backtrack(idx+1, i+1, word) + backtrack(idx + 1, i, word)
        else:
            return backtrack(idx+1, i, word)
t = int(input())
for i in range(t):
    res = str(backtrack(0, 0, input())%10000).zfill(4)
    print(f"Case #{i+1}: {res}")