from math import log2

while True:
    year = int(input())
    if year == 0:
        break
    else:
        doubles = (year - 1960)//10
        bits = 2 ** (2 + doubles)
        max_num = 2**bits - 1
        limit = log2(max_num)
        cur = 0
        n = 1
        while True:
            if cur + log2(n) <= limit:
                cur += log2(n)
                n += 1
            else:
                print(n - 1)
                break