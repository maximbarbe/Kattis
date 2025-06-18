r, c = map(int, input().split(" "))
if r == 1 and c != 1:
    print(0)
elif r == 1 and c== 1:
    print(1)
else:
    ways = r * (r-1)**(c-1)%998244353
    print(ways)