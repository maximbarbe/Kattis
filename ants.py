t = int(input())
for i in range(t):
    length, n = map(int, input().split())
    positions = []
    while len(positions) != n:
        data = [*map(int, input().split())]
        positions += data
    
    min_dist = 0
    max_dist = 0
    for i in range(len(positions)):
        max_dist = max(max_dist, max(positions[i], length - positions[i]))
        min_dist = max(min_dist, min(positions[i], length - positions[i]))
    print(f"{min_dist} {max_dist}")