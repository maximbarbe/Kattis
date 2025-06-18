n, m = map(int, input().split(" "))
obstacles = set()
for i in range(m):
    obstacles.add(int(input()))
for i in range(n):
    if i not in obstacles:
        print(i)
print(f"Mario got {len(obstacles)} of the dangerous obstacles.")