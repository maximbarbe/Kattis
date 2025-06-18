import sys
from collections import defaultdict
definitions = defaultdict(lambda: None)
for line in sys.stdin:
    data = line.strip("\n").split(" ")
    if data[0] == "define":
        definitions[data[2]] = int(data[1])
    else:
        x = data[1]
        op = data[2]
        y = data[3]
        if definitions[x] == None or definitions[y] == None:
            print("undefined")
        else:
            if op == "<":
                if definitions[x] < definitions[y]:
                    print("true")
                else:
                    print("false")
            elif op == ">":
                if definitions[x] > definitions[y]:
                    print("true")
                else:
                    print("false")
            else:
                if definitions[x] == definitions[y]:
                    print("true")
                else:
                    print("false")