from collections import deque;z,l,w,o,a=range,len,input,max,lambda q,x:q.append(x)
def b(s,v,p):
    q,k=[],0;a(q,s)
    while q:
        i,*q=q;v[i]=1;k+=1;x,y,r=p[i]
        for _ in z(l(p)):
            if not v[_]:
                g=p[_];d,u=((x-g[0])**2+(y-g[1])**2)**0.5,g[2]
                if r+u>d>abs(u-r):v[_]=1;a(q,_)
    return k
while 1:
    n,m=int(w()),0
    if n==-1:break
    v,p=[0]*n,[]
    for i in z(n):x,y,r=map(float,w().split());a(p,(x,y,r))
    for i in z(l(p)):
        if not v[i]:m=o(m,b(i,v,p))
    print(f"The largest component contains {m} ring{'s' if m!=1 else ''}.")