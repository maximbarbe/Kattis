from math import inf

num_part, budget, num_hotels, num_weeks = map(int, input().split(" "))
min_cost = inf
for i in range(num_hotels):
    price = int(input())
    beds = [*map(int, input().split(" "))]
    if max(beds) >= num_part:
        if price * num_part <= budget and price * num_part < min_cost:
            min_cost = price * num_part
if min_cost == inf:
    print("stay home")
else:
    print(min_cost)