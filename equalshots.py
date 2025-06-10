a,b=map(int,input().split())
d1,d2=0,0
for i in range(a):
    c,v=map(int,input().split())
    d1 += c*v
for i in range(b):
    c,v=map(int,input().split())
    d2 += c*v
print(("different","same")[d1==d2])