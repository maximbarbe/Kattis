n = int(input())
values = []
numerator = 0
denom = 0
for i in range(n):
    val = int(input())
    
    values.append(val)

values.sort()

sums = [values[0]]
for i in range(1, len(values)):
    sums.append(values[i] + sums[i - 1])

for i in range(len(sums)):
    numerator += (i + 1)*values[i] - sums[i]
    denom += n*values[i]
    

print(numerator/denom)