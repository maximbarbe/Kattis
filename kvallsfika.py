from collections import defaultdict
n=int(input())
p = int(input())
k = int(input())
costs = [*map(int, input().split())]
c = [(costs[i],i) for i in range(len(costs))]
categories = [*map(int, input().split())]
bought = defaultdict(lambda:0)
c.sort(key=lambda el:el[0])
res = 0
for cost, idx in c:
    if cost > p:
        break
    if bought[categories[idx]] < k and cost <= p:
        res += 1
        p -= cost
        bought[categories[idx]] += 1
        
print(res)