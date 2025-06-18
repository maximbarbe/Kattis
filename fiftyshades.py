n = int(input())
res = 0
for i in range(n):
    string = input().lower()
    if "pink" in string or "rose" in string:
        res += 1
if res == 0:
    print("I must watch Star Wars with my daughter")
else:
    print(res)