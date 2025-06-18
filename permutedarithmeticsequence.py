n = int(input())
def is_arithmetic(vals):
    diff = vals[1] - vals[0]
    for i in range(len(vals) - 1):
        if vals[i + 1] - vals[i] != diff:
            return False
        
    return True
def issorted(vals):
    decreasing = True
    increasing = True
    for i in range(len(vals) - 1):
        if vals[i] > vals[i + 1]:
            increasing = False
        if vals[i] < vals[i + 1]:
            decreasing = False
    return decreasing or increasing
for i in range(n):
    vals = [*map(int, input().split(" "))][1:]
    is_sorted = issorted(vals)
    if is_sorted:
        if is_arithmetic(vals):
            print("arithmetic")
        else:
            print("non-arithmetic")
    else:
        vals.sort()
        if is_arithmetic(vals):
            print("permuted arithmetic")
        else:
            print("non-arithmetic")