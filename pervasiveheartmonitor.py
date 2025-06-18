import sys

for line in sys.stdin:
    data = line.split(" ")
    name = []
    values = []
    for i in range(len(data)):
        data[i] = data[i].removesuffix("\n")
        if data[i].isalpha():
            name.append(data[i])
        else:
            values.append(float(data[i]))
    print(f"{sum(values)/len(values)} {' '.join(name)}")