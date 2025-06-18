from collections import defaultdict

n, d = map(int, input().split(" "))
vals = [*map(int, input().split(" "))]

dict = defaultdict(lambda:False)
money = 0
idx = 0
while True:
    if dict[idx] == True:
        break
    money += vals[idx]
    dict[idx] = True
    idx = (idx + d) % n
    
print(money)