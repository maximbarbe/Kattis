n = int(input())
prev = 1
for i in range(n):
    data = input().split(" ")
    x, op, y = data
    x = int(x)
    y = int(y)
    if op == "+":
        res = (x+y)-prev
        prev = res
        print(res)
    elif op == "-":
        res = (x -y)*prev
        prev = res
        print(res)
    elif op == "*":
        res = (x*y)**2
        prev = res
        print(res)
    else:
        if x % 2 == 0:
            x //= 2
        else:
            x = (x+1)//2
        res = x
        print(res)
        prev = res
        