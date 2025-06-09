from collections import defaultdict

n, k = map(int, input().split(" "))
structures = set()
for i in range(n):
    positions = defaultdict(lambda:0)
    vals = [*map(int, input().split(" "))]
    struct = []
    for val in vals:
        if positions[0] == 0:
            positions[0] = val
        else:
            idx = 0
            while True:
                if positions[idx] == 0:
                    positions[idx] = val
                    break
                elif val <= positions[idx]:
                    idx = 2*idx + 1
                else:
                    idx = 2*idx + 2
        
    for k in positions.keys():
        struct.append(k)
    struct.sort()
    structures.add("".join(map(str, struct)))
print(len(structures))