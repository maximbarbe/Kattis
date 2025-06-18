n = int(input())
init = ["{}", "{{}}"]
if n in [0, 1]:
    print(init[n])
    exit()
else:
    for i in range(2, n+1):
        init.append(f"{init[i - 1][:-1]},{init[i -1]}}}")
    print(init[-1])