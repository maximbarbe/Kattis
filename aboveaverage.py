n = int(input())
for i in range(n):
    data = [*map(int, input().split(" "))]
    num = data[0]
    average = sum(data[1:])/num
    above = 0
    for i in range(1, len(data)):
        if data[i] > average:
            above += 1
    percentage = str(round((above/num)*100, 3))
    after_dot = len(percentage.split(".")[1])
    if after_dot != 3:
        percentage += "0" * (3 - after_dot)
    print(f"{percentage}%")