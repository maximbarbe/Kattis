from collections import defaultdict
n,m=map(int, input().split())
menu=[]
for i in range(n):
    menu.append(input())
indices = defaultdict(lambda:0)
for i in range(m):
    customer=input()
    print(menu[indices[customer]])
    indices[customer] += 1
    indices[customer] %= n