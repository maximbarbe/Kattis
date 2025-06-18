n = int(input())
values = []
for i in range(n):
    values.append(int(input()) * pow(4/5, i))
sum_nums = sum(values)
print(sum_nums * 1/5)
averages = [None for i in range(n)]
for i in range(len(values)):
    averages[i] = 1/5 * (sum(values[:i]) + sum(map(lambda el: el/(4/5), values[i + 1:])))
    
print(sum(averages)/n)