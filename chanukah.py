n = int(input())
for i in range(n):
    k, days = map(lambda x: int(x), input().split(" "))
    print(str(k) + " " + str(int(days*(days +1)/2 + days)))