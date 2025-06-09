o=lambda:map(int,input().split());n,k=o();m=[[] for k in range(4)]
for _ in [*o()]:m[_%4]+=[_]
while m[k%4]:
    m[k%4].sort();k+=m[k%4].pop()
print(k)