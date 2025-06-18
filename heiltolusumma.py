n = int(input())

if n > 0:
    print((n * (n+1))//2)
else:
    n = abs(n)
    print(-(n * (n+1))//2 + 1)