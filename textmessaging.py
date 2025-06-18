n = int(input())
for i in range(n):
    res = 0
    max_key, keys, letters = map(int, input().split(" "))
    frequencies = [*map(int, input().split(" "))]
    assigned = [[] for j in range(keys)]
    frequencies.sort(reverse=True)
    for j in range(len(frequencies)):
        assigned[j % len(assigned)].append(1)
        res += frequencies[j] * len(assigned[j % len(assigned)])
    print(f"Case #{i+1}: {res}")