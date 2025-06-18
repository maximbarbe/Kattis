n = int(input())
for i in range(n):
    k = int(input())
    print((8 * pow(9, k-1, 1_000_000_007))%1_000_000_007)