n = int(input())
cities = list(map(int, input().split(" ")))
cities.sort()
final_idx = (n - 1)//2
res = 0
res += sum(cities[final_idx + 1:])
for i in range(final_idx + 1):
    res += cities[i]//2
print(res)