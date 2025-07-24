r, c = map(int, input().split())
cur = 0
for i in range(r):
    s = input()
    if (c - len(s))%2 == 0:
        print("."*((c-len(s))//2) + s + "."*((c-len(s))//2))
    else:
        if cur % 2 == 0:
            print("."*((c-len(s))//2) + s + "."*((c-len(s))//2 + 1))
            
        else:
            print("."*((c-len(s))//2 + 1) + s + "."*((c-len(s))//2))
        cur += 1