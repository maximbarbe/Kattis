au,bu,ar,br = map(int, input().split())
if br == 0:
    if ar >= au:
        print(ar*bu)
    else:
        print(min(au, bu))
        
    exit()
else:
    cur = au
if ar != 0:
    cur += bu + br*ar
print(cur)