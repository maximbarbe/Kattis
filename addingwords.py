from collections import defaultdict
import sys

definitions = dict()
values = defaultdict(lambda: set())


for line in sys.stdin:
    line = line.rstrip()
    line = line.split(" ")
    match line[0]:
        case "def":
            val = int(line[2])
            if definitions.get(line[1], None) == None:
                values[val].add(line[1])
                definitions[line[1]] = val
            else:
                values[definitions[line[1]]].remove(line[1])
                definitions[line[1]] = val
                values[val].add(line[1])
        case "calc":
            expression = line[1:-1]
            for i in range(len(expression)):
                if expression[i] not in "+-":
                    if definitions.get(expression[i], None) == None:
                        print(" ".join(line[1:]) + f" unknown")
                        break
                    else:
                        expression[i] = definitions.get(expression[i], None)
            else:
                res = eval(" ".join(map(str, expression)))
                if len(values[res]) != 1:
                    print(" ".join(line[1:]) + f" unknown")
                else:
                    res = list(values[res])[0]
                    print(" ".join(line[1:]) + f" {res}")
        case _:
            definitions = dict()
            values = defaultdict(lambda: set())