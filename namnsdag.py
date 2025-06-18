name = input()
n = int(input())
res = 0
for i in range(n):
    res += 1
    new_name = input()
    if len(name) != len(new_name):
        continue
    else:
        diff = 0
        for i in range(len(new_name)):
            if name[i] != new_name[i]:
                diff += 1
        if diff <= 1:
            print(res)
            exit()