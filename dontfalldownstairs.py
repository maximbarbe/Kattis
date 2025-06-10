n = int(input())
res = 0
steps = [*map(int, input().split(" "))] + [0]
for i in range(len(steps) - 1):
    if steps[i] != steps[i+1]:
        res += steps[i] - (steps[i + 1]+1)
print(res)