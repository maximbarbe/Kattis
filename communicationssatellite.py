from heapq import*;o,l,h,m=input,range,[],int;n=m(o())
for i in l(n):
    x,y,r=map(m,o().split());h.append((10**9,x,y,r))
h[0],z=(0,h[0][1],h[0][2],h[0][3]),0
while h:
    c,x,y,r=heappop(h);z+= c
    for i in l(len(h)):
        v=h[i];d=((x-v[1])**2+(y-v[2])**2)**0.5-r-v[3]
        if d<v[0]:h[i]=(d,v[1],v[2],v[3])
    heapify(h)
print(z)