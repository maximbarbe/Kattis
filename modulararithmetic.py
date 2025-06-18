from math import gcd

while True:
    n, t = map(int, input().split(" "))
    if n == t == 0:
        break
    for i in range(t):
        data = input().split(" ")
        data[0] = int(data[0])
        data[2] = int(data[2])
        if data[1] == "/":
            
            if gcd(data[2], n) != 1:
                print(-1)
            else:
                print((data[0]%n * pow(data[2], -1, n)%n))
        elif data[1] == "*":
            print(((data[0] % n) * (data[2] % n))%n)
        elif data[1] == "+":
            print((data[0] % n + data[2] %n)%n)
        else:
            print((data[0] % n - data[2] %n)%n)