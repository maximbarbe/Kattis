n = int(input())
res = 1
numbers = []
for i in range(n):
    numbers.append(int(input()))
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        res += 1
print(res)