n, h, c = map(int, input().split())
candles = []
for i in range(n):
    candles.append(sorted([*map(int, input().split())], reverse=True))
candles.sort(key=lambda el:el[-1])
res = 0
while candles[0]:
    candles.sort(key=lambda el:el[-1])
    for i in range(n):
        if candles[i][-1] > c:
            print(res)
            exit()
        else:
            c -= candles[i].pop()
            res += 1
else:
    
    print(n*h)