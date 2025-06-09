import itertools

line =  [*map(int, input().split(" "))]
first = line[6]
sec = line[7]
line = line[:6]
cmb = itertools.combinations(line, 3)

first_tower = set()
sec_tower = set()

for el in cmb:
    if sum(el) == first and len(set(el).intersection(sec_tower)) == 0:
        first_tower = set(el)
    if sum(el) == sec and len(set(el).intersection(first_tower)) == 0:
        sec_tower = set(el)
    
first_tower = list(first_tower)
sec = list(sec_tower)
first_tower.sort(reverse=True)
sec.sort(reverse=True)
print(f"{' '.join(map(str, first_tower))} {' '.join(map(str, sec))}")