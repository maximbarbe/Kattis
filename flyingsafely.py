n = int(input())
for i in range(n):
    m, p = map(int, input().split(" "))
    for j in range(p):
        input()
    print(min([m-1, p]))