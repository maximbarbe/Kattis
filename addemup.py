k={"1":"1","2":"2","5":"5","6":"9","8":"8","9":"6","0":"0"};v=set()
def u(p):
    p=[*p[::-1]]
    for i in range(len(p)):
        if k.get(p[i],7)==7:return None
        p[i]=k.get(p[i])
    return int("".join(p))
n, target = map(int, input().split(" "))
seen = dict()
vals = [*map(int, input().split(" "))]

    

for el in vals:
    temp = u(str(el))
    if temp != None:
        if el in seen.keys() or temp in seen.keys():
            print("YES")
            exit()
        else:
            seen[target - el] = el
            seen[target - temp] = temp
    else:
        if el in seen.keys():
            print("YES")
            exit()
        else:
            seen[target - el] = el
print("NO")