case = 0
while True:
    case += 1
    string = input()
    if string == "END":
        break
    indices = []
    for i in range(len(string)):
        if string[i] == "*":
            indices.append(i)
    if len(indices) == 1:
        print(f"{case} EVEN")
    else:
        diff = indices[1] - indices[0]
        for i in range(1, len(indices) - 1):
            if indices[i + 1] - indices[i] != diff:
                print(f"{case} NOT EVEN")
                break
        else:
            print(f"{case} EVEN")