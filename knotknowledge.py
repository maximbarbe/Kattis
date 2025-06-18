n = int(input())
first = set(input().split(" "))
second = set(input().split(" "))
print(first.difference(second).pop())