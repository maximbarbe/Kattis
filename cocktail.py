n, time = map(int, input().split(" "))
vals = []
for i in range(n):
    vals.append(int(input()))
    
if 0 < max(vals) - (n-1) * time <= min(vals):
    print("YES")
else:
    print("NO")