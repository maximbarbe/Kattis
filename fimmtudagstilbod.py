n = int(input())
if n < 2021:
    print(1000)
else:
    print(1000 + 100 * (n - 2021 + 1))