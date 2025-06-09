from collections import defaultdict
n, q = map(int, input().split(" "))
wealths = dict()
val = 0
for i in range(q):
    command = input().split(" ")
    if command[0] == "SET":
        wealths[int(command[1]) - 1] = command[2]
    elif command[0] == "RESTART":
        wealths =dict()
        val = int(command[1])
    else:
        print(wealths.get(int(command[1]) - 1, val))