wind = int(input())
n = int(input())
for i in range(n):
    data = input().split(" ")
    if int(data[1]) >= wind:
        print(data[0] + " opin")
    else:
        print(data[0] + " lokud")