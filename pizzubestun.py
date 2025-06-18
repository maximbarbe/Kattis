n = int(input())
vals = []
for i in range(n):
    data = input().split(" ")
    vals.append(int(data[1]))
vals.sort(reverse=True)
if n % 2 == 1:
    res = vals[-1]
else:
    res = 0
    
for i in range(n//2):
    res += vals[2*i]
print(res)