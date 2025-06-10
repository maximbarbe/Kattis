from math import inf
n = int(input())
tea_prices = [*map(int, input().split())]
m = int(input())
topping_prices = [*map(int, input().split())]

smallest_price = inf
for i in range(n):
    comb = [*map(int, input().split())]
    for idx in comb:
        if tea_prices[i] + topping_prices[idx - 1] < smallest_price:
            smallest_price = tea_prices[i] + topping_prices[idx - 1]
money = int(input())

if smallest_price > money:
    print(0)
else:
    print(money//smallest_price - 1)