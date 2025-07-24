import sys

for line in sys.stdin.readlines():
    line = line.rstrip()
    one = False
    zero = False
    for c in line:
        for b in bin(ord(c))[2:].zfill(7)[::-1]:
            if b == "1":
                one ^= True
            else:
                zero ^= True
    if one or zero:
        print("trapped")
    else:
        print("free")