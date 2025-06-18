n, m = map(int, input().split())
weights = [*map(int, input().split())]

offers = []
for i in range(m):
    num, ppk = map(int, input().split())
    offers.append((ppk, num))
offers.sort(reverse=True)
weights.sort(reverse=True)
res = 0
i = 0
offers_idx = 0
while i != len(weights) and offers_idx != len(offers):
    currently_sold = 0
    while currently_sold != offers[offers_idx][1] and i != len(weights):
        currently_sold += 1
        res += weights[i] * offers[offers_idx][0]
        i += 1
    offers_idx += 1
print(res)