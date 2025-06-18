wc, hc, ws, hs = map(int, input().split(" "))
if hc - hs >= 2 and wc - ws >= 2:
    print(1)
else:
    print(0)