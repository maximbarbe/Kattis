conversion = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
    "g": 16,
    "h": 17,
    "i": 18,
    "j": 19,
    "k": 20,
    "l": 21,
    "m": 22,
    "n": 23,
    "o": 24,
    "p": 25,
    "q": 26,
    "r": 27,
    "s": 28,
    "t": 29,
    "u": 30,
    "v": 31,
    "w": 32,
    "x": 33,
    "y": 34,
    "z": 35,
    "0": 36
}

inverse = {val:key for key, val in conversion.items()}


def unary(x, y, op, res):
    x_set = set(x)
    y_set = set(y)
    res_set = set(res)
    u = x_set.union(y_set).union(res_set)
    if len(u) != 1 or "1" not in u:
        return False
    x_conv = len(x)
    y_conv = len(y)
    res_conv = len(res)  
    return eval(f"{x_conv}{op}{y_conv}") == res_conv
n = int(input())

for i in range(n):
    data = input().split(" ")

    x = data[0].lower()
    op = data[1].lower()
    y = data[2].lower()

    res = data[-1].lower()

    valid_bases = ""
    
    if unary(x, y, op, res):
        valid_bases += "1"
    for j in range(2, 37):
        try:
            x_conv = int(x, base=j)
            if x_conv < 1 or x_conv > (2**32) - 1:
                continue
            y_conv = int(y, base=j)
            if y_conv < 1 or y_conv > (2**32) - 1:
                continue
            res_conv = int(res, base=j)
            if res_conv < 1 or res_conv > (2**32) - 1:
                continue
            if op == "+":
                if x_conv + y_conv == res_conv:
                    valid_bases += inverse[j]
            elif op == "-":
                if x_conv - y_conv == res_conv:
                    valid_bases += inverse[j]
            elif op == "*":
                if x_conv * y_conv == res_conv:
                    valid_bases += inverse[j]
            else:
                if x_conv % y_conv == 0 and x_conv / y_conv == res_conv:
                    valid_bases += inverse[j]
        except:
            continue
    if valid_bases == "":
        print("invalid")
    else:
        print(valid_bases)