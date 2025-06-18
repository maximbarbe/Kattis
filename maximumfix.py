from collections import defaultdict

n = int(input())

distances = defaultdict(lambda:0)

vals = [*map(int, input().split())]
for i in range(len(vals)):
    dist = abs(((i + 1) - (vals[i]) + n)%n)
    distances[dist] += 1
    
max_amount = 0
max_k = 10**6 + 1
for key, val in distances.items():
    if val > max_amount:
        max_amount = val
        max_k = key
    elif val == max_amount:
        if key < max_k:
            max_k = key
            
print(f"{max_k} {max_amount}")