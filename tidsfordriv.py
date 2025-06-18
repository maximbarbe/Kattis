from collections import defaultdict

n = int(input())

counter = defaultdict(lambda:4)
for i in range(n):
    c = input()
    counter[c[:-1]] -= 1
res = 0
for card in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
    res = max(res, counter[card])
print((res)/(52-n))