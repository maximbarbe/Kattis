from math import comb, factorial

seuil = 10**9
res = 0
n = int(input())
for i in range(1, n+1):
    res += comb(n, i)*factorial(i)
    if res > seuil:
        print("JUST RUN!!")
        exit()
print(res)