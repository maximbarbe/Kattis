a, b, c =map(int, input().split())
operators = ["+", "-", "*", "/"]
res = []
for o1 in operators:
    for o2 in operators:
       res.append((eval(f"{a}{o1}{b}"), eval(f"(({a}{o1}{b}){o2}{c})")))
kept = []
for inter, v in res:
    if v < 0 or int(inter) != inter or int(v) != v:
        continue
    else:
        kept.append(int(v))
print(min(kept))