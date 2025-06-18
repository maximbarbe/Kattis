n = int(input())
string = ""
res = 0
while n != 0:
    string = str(n % 2) + string
    n //= 2
for i in range(len(string)):
    res += int(string[i]) * 2 **i
print(res)
    