m = int(input())
for i in range(m):
    n = int(input())
    if (n == 16):
        print("4 + 4 + 4 + 4 = 16")
    elif n == 8:
        print("4 + 4 + 4 - 4 = 8")
    elif n == 24:
        print("4 + 4 + 4 * 4 = 24")
    elif n == 9:
        print("4 + 4 + 4 / 4 = 9")
    elif n == 0:
        print("4 + 4 - 4 - 4 = 0")
    elif n == -8:
        print("4 + 4 - 4 * 4 = -8")
    elif n == 7:
        print("4 + 4 - 4 / 4 = 7")
    elif n == 68:
        print("4 + 4 * 4 * 4 = 68")
    elif n == 1:
        print("4 + 4 / 4 - 4 = 1")
    elif n == 256:
        print("4 * 4 * 4 * 4 = 256")
    elif n == -16:
        print("4 - 4 - 4 * 4 = -16")
    elif n == -1:
        print("4 - 4 - 4 / 4 = -1")
    elif n == -60:
        print("4 - 4 * 4 * 4 = -60")
    elif n == 32:
        print("4 * 4 + 4 * 4 = 32")
    elif n == 17:
        print("4 * 4 + 4 / 4 = 17")
    elif n == 15:
        print("4 * 4 - 4 / 4 = 15")
    elif n == 60:
        print("4 * 4 * 4 - 4 = 60")
    elif n == 2:
        print("4 / 4 + 4 / 4 = 2")
    elif n == -7:
        print("4 / 4 - 4 - 4 = -7")
    elif n == -15:
        print("4 / 4 - 4 * 4 = -15")
    elif n == 4:
        print("4 + 4 / 4 / 4 = 4")
    elif n == -4:
        print("4 / 4 / 4 - 4 = -4")
    else:
        print("no solution")