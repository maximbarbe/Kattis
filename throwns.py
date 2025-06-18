_=lambda:input().split();i=lambda x:int(x);n,k=map(i,_());c=j=0;m,a,s=_(),-1,[0]
while j!=len(m):
    if m[j][0]!="u":t=i(m[j]);s+=[c:=(c+t)%n];j+=1
    else:s=s[:-i(m[j+1])];c=s[a];j+=2
print(c)