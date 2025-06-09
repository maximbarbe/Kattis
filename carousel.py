while True:
    n, m = map(int, input().split(" "))
    if n == 0 and m == 0:
        break
    offers = []
    for i in range(n):
        quant, price = map(int, input().split(" "))
        offers.append((quant, price))
    offers.sort(key=lambda el:(el[1]/el[0], -el[0]))
    for i in range(len(offers)):
        if offers[i][0] <= m:
            print(f"Buy {offers[i][0]} tickets for ${offers[i][1]}")
            break
    else:
        print("No suitable tickets offered")