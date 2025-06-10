n, dm = map(int, input().split(" "))
data = [*map(int, input().split(" "))]
for i in range(len(data)):
    if data[i] <= dm:
        print(f"It hadn't snowed this early in {i} years!")
        break
else:
    print("It had never snowed this early!")