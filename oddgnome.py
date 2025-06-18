n = int(input())
for i in range(n):
    data =  [*map(int, input().split(" "))]
    m = data[0]
    data = data[1:]
    
    for i in range(1, len(data) - 1):
        if data[i] != data[i - 1] + 1 and data[i] != data[i + 1] - 1:
            print(i + 1)
            break
    else:
        if data[0] != data[1] - 1:
            print(1)
        else:
            print(len(data) + 1)