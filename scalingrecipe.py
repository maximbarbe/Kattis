n, x, y = map(int, input().split(" "))
factor = y/x
for i in range(n):
    print(round(int(input()) * factor))