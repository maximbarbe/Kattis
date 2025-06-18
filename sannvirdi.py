from bisect import bisect


contestants = []
n = int(input())
for i in range(n):
    name, guess = input().split(" ")
    contestants.append((name, int(guess)))
contestants.sort(key= lambda el:el[1])
n = int(input())
for i in range(n):
    q = int(input())
    if q < contestants[0][1]:
        print(":(")
        continue
    idx = bisect(contestants, q, key=lambda el: el[1])
    idx -= 1
    print(contestants[idx][0])