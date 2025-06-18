res = [1, 3]
n = int(input())
if n == 1:
    print(1)
    print(1)
elif n == 2:
    print(3)
    print(4)
else:
    for i in range(3, n+1):
        res.append((i*(i+1)//2))
    print(res[-1])
    print(sum(res))
    