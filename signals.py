from bisect import bisect_left
# Looks like an increasing subsequence problem

n = int(input())
piles = []
for i in range(n):
    new_num = int(input())
    if piles == [] or new_num > piles[-1]:
        piles.append(new_num)
    else:
        piles[bisect_left(piles, new_num)] = new_num
print(len(piles))