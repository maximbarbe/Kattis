l, w = map(int, input().split())
if w > l *26 or w < l:
    print("impossible")
else:
    res = ['a'] * (l)
    w -= l
    for i in range(l):
        if w == 0:
            break
        elif w >= 25:
            res[i] = 'z'
            w -= 25
        else:
            res[i] = chr(ord('a') + w)
            w = 0
    print("".join(res))