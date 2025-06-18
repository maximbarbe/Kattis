from collections import defaultdict

n = int(input())
for i in range(n):
    k = input()
    guests = defaultdict(lambda: 0)
    g = input().split(" ")
    for guest in g:
        if guests[guest] == 0:
            guests[guest] += 1
        else:
            guests[guest] -= 1
    
    for key in guests.keys():
        if guests[key] == 1:
            print(f"Case #{i+1}: {key}")