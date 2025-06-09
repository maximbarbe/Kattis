n = int(input())
knights = []
for i in range(1, n+1):
    hp, strength = map(int, input().split(" "))
    knights.append((hp, strength, i))
    
while len(knights) != 1:
    first = knights.pop(0)
    sec = knights.pop(0)
    first_hp = first[0]
    sec_hp = sec[0]
    while True:
        sec_hp -= first[1]
        if sec_hp <= 0:
            knights.insert(0, (first_hp, first[1], first[2]))
            break
        first_hp -= sec[1]
        if first_hp <= 0:
            knights.insert(0, (sec_hp, sec[1], sec[2]))
            break
print(knights[0][-1])