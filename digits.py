x_0 = None

while val := input():
    if val.isnumeric() == False:
        break
    x_0 = val
    i = 0
    while True:
        i += 1
        x_i = str(len(x_0))
        if x_i == x_0:
            print(i)
            break
        x_0 = x_i