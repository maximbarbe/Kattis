from math import e, pi, log2


# https://web.cecs.pdx.edu/~maier/cs584/Lectures/lect07b-11-MG.pdf
def fft(vals, invert):
    n = len(vals)
    if n == 1:
        return [vals[0]]
    exponent = 2*pi*1j/n
    exponent *= 1 if invert == False else -1
    wn = pow(e, exponent)
    w = 1
    evens = vals[::2]
    odds = vals[1::2]
    ye = fft(evens, invert)
    yo = fft(odds, invert)
    for i in range(n//2):
        vals[i] = ye[i] + w*yo[i]
        vals[i + n//2] = ye[i] - w*yo[i]
        w = w*wn
    return vals
    
n, m = map(int, input().split())
a = [*map(int, input().split())]
b = [*map(int, input().split())]
next_power = log2(len(a) + len(b))
if int(next_power) != next_power:
    next_power = int(next_power) + 1
else:
    next_power = int(next_power)


a = a + [0]*(2**next_power - len(a))
b = b + [0]*(2**next_power - len(b))


a = fft(a, invert=False)
b = fft(b, invert=False)
res = []
for i in range(len(a)):
    res.append(a[i] * b[i])

res = fft(res, True)
for i in range(len(res)):
    res[i] = round(res[i].real/len(a))

while res and res[-1] == 0:
    res.pop()
if not res:
    res.append(0)
print(*res)