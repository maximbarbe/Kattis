n=int(input())
res=0
for i in range(n):
    input()
    res += int(input())
if res < 0:
    print("Nekad")
elif res > 0:
    print("Usch, vinst")
else:
    print("Lagom")