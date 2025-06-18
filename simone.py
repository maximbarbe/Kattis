n, k = map(int, input().split(" "))
freq = dict()
for i in range(1, k+1):
    freq[i] = 0
    
vals = [*map(int, input().split(" "))]
for i in range(len(vals)):
    freq[vals[i]] += 1
min_freq = min(freq.values())
res = [key for key, val in freq.items() if val == min_freq]
print(len(res))
print(" ".join(map(str, res)))