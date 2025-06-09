n = int(input())
for i in range(n):
    input()
    m = int(input())
    candies = 0
    for i in range(m):
        candies += int(input())
    if candies % m == 0:
        print("YES")
    else:
        print("NO")