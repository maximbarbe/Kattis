n = int(input())
vals = [*map(int, input().split())]
indices = {vals[i]:i+1 for i in range(len(vals))}
res = [indices[key] for key in sorted(indices.keys(), reverse=True)]
print(*res)