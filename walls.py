from itertools import combinations
from math import dist, inf

l, w, n, r = map(int, input().split())
min_number = inf

centers = {
    (-l/2, 0): False,
    (l/2, 0): False,
    (0, -w/2): False,
    (0, w/2):False
}

cranes = []
for i in range(n):
    x, y = map(int, input().split())
    cranes.append((x, y))
    

for comb in combinations(cranes, 4):
    for c in comb:
        for coord in centers.keys():
            if dist(coord, c) <= r:
                centers[coord] = True
                
    else:
        for val in centers.values():
            if val == False:
                for key in centers.keys():
                    centers[key] = False
                break
        else:
            min_number = 4
            for key in centers.keys():
                centers[key] = False
            break
    
for comb in combinations(cranes, 3):
    for c in comb:
        for coord in centers.keys():
            if dist(coord, c) <= r:
                centers[coord] = True
                
    else:
        for val in centers.values():
            if val == False:
                for key in centers.keys():
                    centers[key] = False
                break
        else:
            min_number = 3
            for key in centers.keys():
                centers[key] = False
            break
        
for comb in combinations(cranes, 2):
    for c in comb:
        for coord in centers.keys():
            if dist(coord, c) <= r:
                centers[coord] = True
                
    else:
        for val in centers.values():
            if val == False:
                for key in centers.keys():
                    centers[key] = False
                break
        else:
            min_number = 2
            for key in centers.keys():
                centers[key] = False
            break
for comb in combinations(cranes, 1):
    for c in comb:
        for coord in centers.keys():
            if dist(coord, c) <= r:
                centers[coord] = True
                
    else:
        for val in centers.values():
            if val == False:
                for key in centers.keys():
                    centers[key] = False
                break
        else:
            min_number = 1
            for key in centers.keys():
                centers[key] = False
            break
    
if min_number == inf:
    print("Impossible")
else:
    print(min_number)