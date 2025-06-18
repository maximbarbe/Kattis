# Binary search to find the highest power, then go from there all the way to 1

n = int(input())
start, end = 1, 128
while start < end:
    mid = (start + end)//2
    if (mid**9) < n:
        start = mid + 1
    else:
        end = mid
        
for i in range(start, 0, -1):
    if n % (i **9) == 0:
        print(i)
        exit()