k = int(input()) - 1
n = int(input())
time_limit = 210
cur = 0
for i in range(n):
    data = input().split(" ")
    if cur + int(data[0]) > time_limit:
        print(k + 1)
        exit()
    else:
        cur += int(data[0])
        if data[1] == "T":
            k += 1
            k %= 8
print((k + 1)%8)