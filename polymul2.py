from math import log2, pi, e


def fft(vals, invert):
    n = len(vals)
    if n == 1:
        return [vals[0]]
    ye = fft(vals[::2], invert)
    yo = fft(vals[1::2], invert)
    exponent = 2*pi*1j/n
    exponent *= 1 if not invert else -1
    w = 1
    wn = pow(e, exponent)
    for i in range(n//2):
        vals[i] = ye[i] + w*yo[i]
        vals[i + n//2] = ye[i] - w*yo[i]

        w = w*wn
    return vals


input()
n = int(input())
a=[*map(int, input().split())]
m = int(input())
b=[*map(int, input().split())]

log_2 = log2(len(a) + len(b))

if int(log_2) == log_2:
    next_power = int(log_2)
else:
    next_power = int(log_2) + 1

a.extend([0] * (2**next_power - len(a)))
b.extend([0] * (2**next_power - len(b)))

a = fft(a, False)
b = fft(b, False)

res = []
for i in range(len(a)):
    res.append(a[i]*b[i])
res = fft(res, True)
for i in range(len(res)):
    res[i] = round(res[i].real/len(a))
while len(res) != n+m+1:
    res.pop()

print(len(res) - 1)
print(*res)