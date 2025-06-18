first = [*map(int, [char for char in input()])]
second =[*map(int, [char for char in input()])]



if len(first) < len(second):
    first = [0 for i in range(len(second) - len(first))] + first
elif len(second) < len(first):
    second = [0 for i in range(len(first) - len(second))] + second
    
res_first = []
res_second = []
for i in range(len(first)):
    if first[i] < second[i]:
        res_second.append(second[i])
    elif second[i] < first[i]:
        res_first.append(first[i])
    else:
        res_second.append(second[i])
        res_first.append(first[i])
if len(res_first) == 0:
    print("YODA")
else:
    print(int("".join(map(str, res_first))))
if len(res_second) == 0:
    print("YODA")
else:
    print(int("".join(map(str, res_second))))