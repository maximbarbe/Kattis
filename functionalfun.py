while True:
    try:
        _, *domain = input().split()
        _, *codomain = input().split()
    except EOFError:
        break
    c = dict()
    d = dict()
    for el in domain:
        d[el] = []
    for el in codomain:
        c[el] = []
    injective = True
    surjective = True
    not_func = False
    n = int(input())
    for i in range(n):
        src, dest = input().split(" -> ")
        d[src].append(dest)
        c[dest].append(src)
    for v in c.values():
        if len(v) > 1:
            injective = False
        elif len(v) == 0:
            surjective = False
    for v in d.values():
        if len(v) > 1:
            not_func = True
            
    if not_func:
        print("not a function")
    elif surjective and injective:
        print("bijective")
    elif surjective:
        print("surjective")
    elif injective:
        print("injective")
    else:
        print("neither injective nor surjective")