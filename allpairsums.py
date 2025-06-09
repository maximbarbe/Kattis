from math import e, pi, log2



def fft(vals, invert):
    
    n = len(vals)
    if n == 1:
        return [vals[0]]
    exponent = 2*pi*1j/n
    exponent *= 1 if invert == False else -1
    w = 1
    wn = pow(e, exponent)
    ye = fft(vals[::2], invert)
    yo = fft(vals[1::2], invert)
    
    for i in range(n//2):
        vals[i] = ye[i] + w*yo[i]
        vals[i + n//2] = ye[i] - w*yo[i]
        w = w*wn
    return vals



n, m = map(int, input().split())

a = [*map(int, input().split())]
b = [*map(int, input().split())]
a_poly = [0] * (2*10**5 + 1)
b_poly = [0] * (2*10**5 + 1)

for i in range(len(a)):
    a_poly[10**5 + a[i]] += 1
    
for i in range(len(b)):
    b_poly[10**5 + b[i]] += 1

log_2 = log2(len(a_poly) + len(b_poly))

if int(log_2) == log_2:
    next_power = int(log_2)
else:
    next_power = int(log_2) + 1

a_poly.extend([0] * (2**next_power - len(a_poly)))
b_poly.extend([0] * (2**next_power - len(b_poly)))

a_poly = fft(a_poly, False)
b_poly = fft(b_poly, False)
res = []
for i in range(len(a_poly)):
    res.append(a_poly[i] * b_poly[i])
    
res = fft(res, True)
for i in range(len(res)):
    res[i] = round(res[i].real/len(a_poly))
q = int(input())
for i in range(q):
    query = int(input())
    if query < -2*10**5 or query > 2*10**5:
        print(0)
    else:
        print(res[2*10**5 + query])