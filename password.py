n = int(input())
probabilities = []
for i in range(n):
    data = input().split(" ")
    probabilities.append(float(data[1]))
probabilities.sort(reverse=True)
res = 0
for i in range(len(probabilities)):
    res += probabilities[i] * (i + 1)
print(res)