from collections import defaultdict

n = int(input())
balloons = [*map(int, input().split(" "))]

arrows_thrown = defaultdict(lambda: 0)

res = 0

for i in range(len(balloons)):
    if arrows_thrown[balloons[i]] != 0:
        arrows_thrown[balloons[i]] -= 1
        if balloons[i] - 1 != 0:
            arrows_thrown[balloons[i] - 1] += 1
    else:
        res += 1
        arrows_thrown[balloons[i] - 1] += 1
            
print(res)