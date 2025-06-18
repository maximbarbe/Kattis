n = int(input())

for i in range(n):
    print(str(bin(int(input()) + 1)[3:]))