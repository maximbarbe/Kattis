n = int(input())

if 1 <= n <= 99:
    print(99)
elif 100 <= n <= 999:
    lower = (n // 100) * 100 - 1
    upper = (n // 100 + 1) * 100 - 1
    if (abs(lower - n) < abs(upper - n)):
        print(lower)
    else:
        print(upper)
else:
    lower = (n // 100) * 100 - 1
    upper = (n // 100 + 1) * 100 - 1
    if (abs(lower - n) < abs(upper - n)):
        print(lower)
    else:
        print(upper) 