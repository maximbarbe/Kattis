_=lambda:map(int, input().split());k,r=_();g=[*_()];m=0;
for i in range(r):
    *v,c=_();b=10**9
    for j in range(k):
        if v[j]!=0:b=min(b,g[j]//v[j])
    m=max(m,b*c)
print(m)