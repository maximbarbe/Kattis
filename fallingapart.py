n = int(input())


alice = 0
bob = 0
data = [*map(int, input().split(" "))]
data.sort(reverse=True)
for i in range(len(data)):
    if i % 2 == 0:
        alice += data[i]
    else:
        bob += data[i]
        
print(f"{alice} {bob}")