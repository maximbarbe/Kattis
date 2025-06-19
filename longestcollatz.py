from functools import lru_cache


@lru_cache(None)
def get_res(n):
    if n == 1:
        return 0
    if n%2 == 0:
        return 1 + get_res(n//2)
    else:
        return 1 + get_res(3*n + 1)
    
res =0 
maximum = 0
for i in range(1, int(input()) +1):
    c = get_res(i)
    if c > maximum:
        maximum = c
        res = i
print(res)