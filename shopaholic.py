n = int(input())
prices = [*map(int, input().split(" "))]
prices.sort(reverse=True)
discount = 0
for i in range(0, len(prices) - 2, 3):
    discount += prices[i + 2]
print(discount)