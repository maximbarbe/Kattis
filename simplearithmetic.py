import decimal
decimal.getcontext().prec = 100
a, b, c = map(lambda el:decimal.Decimal(int(el)), input().split(" "))
print((a *b)/c)