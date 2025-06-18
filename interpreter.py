import sys
registers = [0]*10

res = 0
ram = []
for line in sys.stdin:
    line = line.rstrip()
    ram.append(int(line))
if len(ram) == 0:
    print(0)
    exit()
ram = ram + [0]*(1000 - len(ram))
idx = 0
while True:
    cur = str(ram[idx]).zfill(3)
    x = int(cur[1])
    y = int(cur[2])
    match cur[0]:
        case "1":
            res += 1
            print(res)
            exit()
        case "2":
            registers[x] = y
            res += 1
        case "3":
            registers[x] += y
            registers[x] %= 1000
            res += 1
        case "4":
            registers[x] *= y
            registers[x] %= 1000
            res += 1
        case "5":
            registers[x] = registers[y]
            res += 1
        case "6":
            registers[x] += registers[y]
            registers[x] %= 1000
            res += 1
        case "7":
            registers[x] *= registers[y]
            registers[x] %= 1000
            res += 1
        case "8":
            registers[x] = ram[registers[y]]
            res += 1
        case "9":
            ram[registers[y]] = registers[x]
            res += 1
        case _:
            if registers[y] != 0:
                idx = registers[x]
                res += 1
                idx -= 1
            else:
                res += 1
    idx += 1