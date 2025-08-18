res = True
for i in range(int(input())):
    if int(input()) < 48:
        res = False
    res = res and True
print(str(res))