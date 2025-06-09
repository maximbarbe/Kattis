n  = int(input())
res = 0
for i in range(n):
    string = input()
    if "CD" not in string:
        res += 1
print(res)