while True:
    n = int(input())
    if n == 0:
        break
    registers = ["?" for i in range(32)]
    for i in range(n):
        data = input().split(" ")
        if data[0] == "SET":
            registers[31 - int(data[1])] = 1
        elif data[0] == "CLEAR":
            registers[31 - int(data[1])] = 0
        elif data[0] == "OR":
            j, k = int(data[1]), int(data[2])
            if registers[31 - j] == 1 or registers[31 - k] == 1:
                registers[31 - j] = 1
            elif registers[31 - j] == 0 and registers[31 - k] == 0:
                continue
            elif registers[31 - j] == "?" or registers[31 -k] == "?":
                registers[31 - j] = "?"
        else:
            j, k = int(data[1]), int(data[2])
            if registers[31 - j] == 0 or registers[31 - k] == 0:
                registers[31 - j] = 0
            elif registers[31 - j] == 1 and registers[31 - k] == 1:
                continue
            elif registers[31 - j] == "?" or registers[31 -k] == "?":
                registers[31 - j] = "?"
    print("".join(map(str, registers)))