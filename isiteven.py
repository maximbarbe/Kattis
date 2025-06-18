n, k = map(int, input().split())
divide = pow(2, k)
cur = 1
for i in range(n):
    cur = ((cur%divide) * (int(input())%divide))%divide
    
if cur == 0:
    print(1)
else:
    print(0)