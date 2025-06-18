L, n = map(int, input().split(" "))
cur = 0
left = 0
for i in range(n):
    data = input().split(" ")
    if data[0] == "leave":
        cur -= int(data[1])
    else:
        group = int(data[1])
        if cur + group > L:
            left += 1
        else:
            cur += group
print(left)