n, s = map(int, input().split(" "))
temp = s
res = 0
for i in range(n):
    data = input()
    needed = 0
    if not data[-1].isnumeric():
        needed = int(data[:-1])  + 1
    else:
        needed = int(data)
    if temp - needed < 0:
        res += 1
        temp = s
        temp -= needed
    else:
        temp -= needed
print(res)