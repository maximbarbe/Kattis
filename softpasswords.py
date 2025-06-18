S = input()
P = input()
if S == P:
    print("Yes")
elif S[1:] == P and S[0].isnumeric():
    print("Yes")
elif S[:-1] == P and S[-1].isnumeric():
    print("Yes")
else:
    converted = ""
    for i in range(len(P)):
        if P[i].isnumeric():
            converted += P[i]
        else:
            if P[i].islower():
                converted += P[i].upper()
            else:
                converted += P[i].lower()
    if converted == S:
        print("Yes")
    else:
        print("No")