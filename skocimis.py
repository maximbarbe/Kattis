a, b, c = map(int, input().split(" "))
jumps = 0
while True:
    if b - a != 1 or c - b != 1:
        if c - b >= b - a:
            jumps += 1
            a, b = b, c - 1
        else:
            jumps += 1
            b, c = a+1, b
    else:
        print(jumps)
        break