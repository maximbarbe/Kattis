from math import dist
n =  int(input())
dict = {
    "rectangle": [],
    "circle": []
}
for i in range(n):
    data = input().split(" ")
    if data[0] == "rectangle":
        dict["rectangle"].append([(int(data[1]), int(data[2])), (int(data[3]), int(data[4]))])
    else:
        dict["circle"].append([(int(data[1]), int(data[2])), int(data[3])])
for m in range(int(input())):
    x, y = map(int, input().split(" "))
    res = 0
    for rec in dict["rectangle"]:
        if rec[0][0] <= x <= rec[1][0] and rec[0][1] <= y <= rec[1][1]:
            res += 1
    for circ in dict["circle"]:
        if dist((x, y), circ[0]) <= circ[1]:
            res += 1
    print(res)