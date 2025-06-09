while n:=int(input()):
    r,l,m=0,set(),{}
    for i in[1]*n:
        _,h=input(),0;l|={_}
        for c in _:h^=ord(c)
        h%=256
        if h in m:r+=sum(1 for k in m[h] if _!=k);m[h]+=[_]
        else:m[h]=[_]
    print(len(l),r)