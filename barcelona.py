n, k = map(int, input().split(" "))
data = [*map(int, input().split(" "))]

idx = data.index(k)
if idx == 0:
    print("fyrst")
elif idx == 1:
    print("naestfyrst")
else:
    print(f"{idx + 1} fyrst")