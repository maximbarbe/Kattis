i=lambda:input();y=lambda b:int(b);t=y(i());m=lambda x,y:range(x,y);a=47
for _ in m(0,t):
    i();o=y(i());v=[*map(y,i().split())];p=r=0;s={0:1}
    for j in m(0,o):
        z=p+v[j]
        if z-a in s:r+=s[z-a]
        s[z]=s.get(z,0)+1;p=z
    print(r)