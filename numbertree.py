data = input().split(" ")
nodes = 2**(int(data[0]) + 1)
cur = 1
string = data[1]
for i in range(len(string)):
    if string[i] == "L":
        cur *= 2
    else:
        cur = cur*2 + 1
print(nodes - cur)