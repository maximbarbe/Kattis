n = int(input())
numbers = list(map(int, input().split(" ")))
res = [numbers[0]]
for i in range(1, len(numbers)):
    if numbers[i] > res[-1]:
        res.append(numbers[i])
print(len(res))
print(" ".join(list(map(str, res))))