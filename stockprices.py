import heapq

n = int(input())
for i in range(n):
    m = int(input())
    ask_prices = []
    bid_prices = []
    stock_prices = []
    for i in range(m):
        data = input().split(" ")
        if data[0] == "buy":
            quant = int(data[1])
            price = int(data[4])
            if ask_prices != []:
                while ask_prices != [] and ask_prices[0][0] <= price and quant != 0:
                    cur = heapq.heappop(ask_prices)
                    ask_p = cur[0]
                    ask_q = cur[1]
                    if ask_q > quant:
                        ask_q -= quant
                        quant = 0
                        stock_prices.append(ask_p)
                        heapq.heappush(ask_prices, (ask_p, ask_q))
                    elif ask_q == quant:
                        quant = 0
                        stock_prices.append(ask_p)
                    else:
                        quant -= ask_q
                        stock_prices.append(ask_p)
            if quant != 0:
                heapq.heappush(bid_prices, (-price, quant))
        else:
            quant = int(data[1])
            price = int(data[4])
            if bid_prices != []:
                while bid_prices != [] and -bid_prices[0][0] >= price and quant != 0:
                    cur = heapq.heappop(bid_prices)
                    bid_p = -cur[0]
                    bid_q = cur[1]
                    if bid_q > quant:
                        bid_q -= quant
                        quant = 0
                        stock_prices.append(price)
                        heapq.heappush(bid_prices, (-bid_p, bid_q))
                    elif bid_q == quant:
                        quant = 0
                        stock_prices.append(price)
                    else:
                        quant -= bid_q
                        stock_prices.append(price)
            if quant != 0:
                heapq.heappush(ask_prices, (price, quant))
        print(f"{'-' if ask_prices == [] else ask_prices[0][0]} {'-' if bid_prices == [] else -bid_prices[0][0]} {'-' if stock_prices == [] else stock_prices[-1]}")