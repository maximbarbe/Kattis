n = int(input())
res = 0
for i in range(n):
    num = input()
    res += int(num[:-1])**(int(num[-1]))
print(res)