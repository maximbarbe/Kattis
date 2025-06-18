n = int(input())
days = set()
res = 0
for i in range(n):
    begin, end = map(int, input().split(" "))
    days.update(set(range(begin, end + 1)))
print(len(days))