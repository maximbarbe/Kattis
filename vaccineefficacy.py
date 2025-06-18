va=[0]*3;nv=[0]*3
vac=nonvac=0
for i in range(int(input())):
    v,a,b,c=[*input()]
    if v=="Y":
        vac += 1
        if a=="Y":va[0]+=1
        if b=="Y":va[1]+=1
        if c=="Y":va[2]+=1
    else:
        nonvac+=1
        if a=="Y":nv[0]+=1
        if b=="Y":nv[1]+=1
        if c=="Y":nv[2]+=1
for i in range(3):
    if nv[i]/nonvac<=va[i]/vac:
        print("Not Effective")
    else:
        print((1 - (va[i]/vac)/(nv[i]/nonvac))*100)