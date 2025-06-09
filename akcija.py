n = int(input())
values = []
for i in range(n):
    values.append(int(input()))
values.sort(reverse=True)
res = 0
for i in range(len(values)):
    if i % 3 != 2:
        res += values[i]
        
print(res)