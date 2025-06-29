w = 230_309_227
k = 68_431_307
MOD = 2**64
for i in range(100):
    y = int(input())
    cur = (y-k)%MOD
    print((pow(w, -1, MOD)*cur)%(MOD))