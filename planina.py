cur = 4
side = 2
n = int(input())
if n == 0:
    print(cur)
    exit()
for i in range(n):
    side = (2 * side - 1)
    cur = side ** 2 
print(cur)