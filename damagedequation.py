op = ["*", "+", "-", "//"]

a, b, c, d = map(int, input().split(" "))
verbose = False
for i in range(len(op)):
    if op[i] == "//" and b == 0:
        continue
    for j in range(len(op)):
        if op[j] == "//" and d == 0:
            continue
        expr = f"{a} {op[i]} {b} == {c} {op[j]} {d}"
        if eval(expr):
            print(f"{a} {'/' if op[i] == '//' else op[i]} {b} = {c} {'/' if op[j] == '//' else op[j]} {d}")
            verbose = True
            
if not verbose:
    print("problems ahead")