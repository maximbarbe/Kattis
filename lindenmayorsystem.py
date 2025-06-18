n, m = map(int, input().split(" "))
rules = dict()
for i in range(n):
    src, dest = input().split(" -> ")
    rules[src] = dest
    
res = input()
for i in range(m):
    temp = res 
    res = ""
    for char in temp:
        res += rules.get(char, char)
print(res)