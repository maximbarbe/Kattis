i=lambda:input();t=int(i());v=[];
def b(i,v,c):
    if i==len(v):print(" ".join(c))
    else:
        for w in v[i]:
            c.append(w);b(i+1,v,c);c.pop()
for _ in range(t):
    n,*w=i().split();v.append(sorted(w))
b(0,v,[])