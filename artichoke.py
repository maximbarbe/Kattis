from math import sin, cos, inf

def price(k, a, b, c, d, p):
    return p * (sin(a*k + b) + cos(c*k + d) + 2)

p, a, b, c, d, n = map(int, input().split(" "))
stock_prices = []
for i in range(1, n+1):
    stock_prices.append(price(i, a, b, c, d, p))
    
if n == 1:
    print(0)
    exit()
else:
    max_price = stock_prices[0]
    max_diff = -inf
    for i in range(1, len(stock_prices)):
        if -(stock_prices[i] - max_price) > max_diff:
            max_diff = -(stock_prices[i] - max_price)
        if stock_prices[i] > max_price:
            max_price = stock_prices[i]
    if max_diff < 0:
        print(0)
    else:
        print(max_diff)