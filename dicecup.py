probabilities = {
    
}
n, m = map(lambda x: int(x), input().split(" "))
outcomes = m * n
for i in range(2, m * n + 1):
    probabilities[i] = 0

outcome = set()
for i in range(1, n+ 1):
    for j in range(1, m + 1):
        outcome.add((i, j))
for item in outcome:
    probabilities[sum(item)] += 1/outcomes
max_values = max(probabilities.values())

for key, value in probabilities.items():
    if value == max_values:
        print(key)