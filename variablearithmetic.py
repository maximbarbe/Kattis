from collections import defaultdict

definitions = defaultdict(lambda:None)
while True:
    line = input()
    if line == "0":
        break
    if "=" in line:
        data = line.split(" = ")
        definitions[data[0]] = int(data[1])
    else:
        terms = line.split(" + ")
        values = []
        variables = []
        for v in terms:
            if v.isnumeric():
                values.append(int(v))
            else:
                if definitions[v] != None:
                    values.append(definitions[v])
                else:
                    variables.append(v)
        if len(values) != 0:
            variables.insert(0, sum(values))
        print(" + ".join(map(str, variables)))