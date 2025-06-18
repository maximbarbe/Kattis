n, m, p = map(int, input().split(" "))
if n + m == p:
    print(f"{n}+{m}={p}")
    exit()
elif n - m == p:
    print(f"{n}-{m}={p}")
    exit()
elif n*m == p:
    print(f"{n}*{m}={p}")
    exit()
elif n/m == p:
    print(f"{n}/{m}={p}")
    exit()
elif n == m + p:
    print(f"{n}={m}+{p}")
    exit()
elif n == m - p:
    print(f"{n}={m}-{p}")
    exit()
elif n == m * p:
    print(f"{n}={m}*{p}")
    exit()
else:
    print(f"{n}={m}/{p}")
    exit()