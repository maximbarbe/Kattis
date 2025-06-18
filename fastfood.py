from collections import Counter
from math import inf
n = int(input())
for i in range(n):
    types_prizes, types_stickers = map(int, input().split(" "))
    prizes = []
    for i in range(types_prizes):
        data = [*map(int, input().split(" "))]
        prizes.append(data[1:])
    stickers = [*map(int, input().split(" "))]
    res = 0 
    for prize in prizes:
        min_amount = inf
        for i in range(len(prize) - 1):
            if prize[i] - 1 >= len(stickers):
                min_amount = 0
                break
            else:
                if stickers[prize[i] - 1] < min_amount:
                    min_amount = stickers[prize[i] - 1]
        res += min_amount * prize[-1]
    print(res)