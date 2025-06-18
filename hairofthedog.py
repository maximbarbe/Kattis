n = int(input())
prev=input()
c= 0
for i in range(n-1):
    cur=input()
    if prev == "drunk" and cur=="sober":
        c+=1
    prev = cur
print(c)