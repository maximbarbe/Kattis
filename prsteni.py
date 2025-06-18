from math import gcd
n = int(input())
data = list(map(int, input().split(" ")))
for i in range(1, len(data)):
    if data[0]%data[i] == 0:
        print(f"{data[0]//data[i]}/1")
    else:
        num = gcd(data[0], data[i])
        print(f"{data[0]//num}/{data[i]//num}")