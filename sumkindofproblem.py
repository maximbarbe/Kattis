P = int(input())
for i in range(P):
    K, n = map(int, input().split(" "))
    print(f"{K} {int(n*(n+1)/2)} {n**2} {n*(n+1)}")