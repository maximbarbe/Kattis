n = int(input())
for i in range(n):
    s, d = map(int, input().split(" "))
    if d > s or (s+d)%2 == 1:
        print("impossible")
    else:
        first = (s + d)//2
        sec = (s-d)//2
        print(f"{first} {sec}")