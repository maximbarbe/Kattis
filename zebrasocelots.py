n= int(input())

animals = []
for i in range(n):
    animals.append(input())
    
times = [0 for i in range(n)]
times[-1] = 1
for i in range(n-2, -1, -1):
    times[i] = 1 + sum(times[i+1:])
    
res = 0
for i in range(len(animals)):
    if animals[i] == 'O':
        res += times[i]
        
print(res)