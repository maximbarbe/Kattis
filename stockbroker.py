def res(money, shares, buy, idx):
    if idx == len(vals):
        return money + shares * buy
    else:
        if vals[idx] >= buy:
            money_after_selling = money + shares * vals[idx]
            bought_shares = min(100000, money_after_selling//vals[idx])
            money_after_selling -= bought_shares*vals[idx]
            return res(money_after_selling, bought_shares, vals[idx], idx + 1)
        else:
            money_after_selling = money + shares * buy
            bought_shares = min(100000, money_after_selling//vals[idx])
            money_after_selling -= bought_shares*vals[idx]
            return res(money_after_selling, bought_shares, vals[idx], idx + 1)

d = int(input())
vals = [int(input()) for i in range(d)]

print(res(100, 0, 10**6, 0))