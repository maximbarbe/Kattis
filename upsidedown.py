n = int(input())
words = input().split()
print(*sorted([*map(lambda w:w[::-1], words)], reverse=True))