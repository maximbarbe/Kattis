from math import dist

while True:
    data = input().split(" ")
    distance = float(data[0])
    n = int(data[1])
    if distance == 0 and n == 0:
        break
    sweet = [True for i in range(n)]
    num_sweets = n
    num_sour = 0
    points = []
    for i in range(n):
        points.append(tuple(map(float, input().split(" "))))
        
    for i in range(n - 1):
        for j in range(i + 1, n):
            if dist(points[i], points[j]) <= distance:
                if sweet[i] == True:
                    num_sweets -= 1
                    num_sour += 1
                    sweet[i] = False
                if sweet[j] == True:
                    num_sweets -= 1
                    num_sour += 1
                    sweet[j] = False
    print(f"{num_sour} sour, {num_sweets} sweet")