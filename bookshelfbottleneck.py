k=lambda:map(int,input().split());n,H=k();r=t=0
while n:a,b,c=sorted(k());t|=a>H;r+=(a,b)[b>H];n-=1
print((r,"impossible")[t])