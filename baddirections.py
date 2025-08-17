t = int(input())
for i in range(t):
    k, n = input().split()
    k = int(k)
    res = "".join([str((int(char) + k)%10) for char in n])
    print(res)