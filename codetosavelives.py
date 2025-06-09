n = int(input())
for i in range(n):
    x = int("".join(input().split(" ")))
    y = int("".join(input().split(" ")))
    xy = x + y
    xy = [char for char in str(xy)]
    print(" ".join(xy))