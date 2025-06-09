t = int(input())
for i in range(t):
    input()
    n = int(input())
    ranks = []
    for j in range(n):
        name, s = input().split()
        s = int(s)
        ranks.append(s)
    ranks.sort()
    res = 0
    for i in range(len(ranks)):
        res += abs(i + 1 - ranks[i])
    print(res)