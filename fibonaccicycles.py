from collections import defaultdict

fib = [1, 1]
while len(fib) != 1000:
    fib.append(fib[-1] + fib[-2])

for i in range(int(input())):
    q = int(input())
    freq = defaultdict(lambda: 0)
    seen = defaultdict(lambda: None)
    minimum = 1001
    for j in range(2, 1000):
        res = fib[j] % q
        freq[res] += 1
        if freq[res] == 2:
            print(seen[res])
            break
        else:
            seen[res] = j