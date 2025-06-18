packages, stores = map(int, input().split(" "))
vals = [*map(int, input().split(" "))]

versions = dict()
for i in range(packages):
    data = input().split(" ")
    versions[data[0]] = int(data[1])
for val in vals:
    res = 0
    for i in range(val):
        data = input().split(" ")
        if data[0] in versions:
            res += versions[data[0]] - int(data[1])
    print(res)