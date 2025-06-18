distinct = set()
for i in range(10):
    num = int(input())
    distinct.add(num % 42)
print(len(distinct))