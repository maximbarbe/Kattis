n = int(input())
steps = 0
while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n += 2*n + 1
    steps += 1
print(steps)