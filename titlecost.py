name, cost = input().split(" ")
if len(name) < float(cost):
    print(len(name))
else:
    print(float(cost))