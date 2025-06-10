a = input()
b = input()
if len(a) < len(b):
    a = "0" * (len(b) - len(a)) + a
if len(b) < len(a):
    b = "0" * (len(a) - len(b)) + b

res = 0
for i in range(len(a)):
    if a[i] == b[i] == "1":
        res += 1
    elif b[i] == "1" and a[i] == "0":
        res += len(a) - i
        break
print(res)