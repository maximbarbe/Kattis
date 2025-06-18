from math import inf

largest_box = -inf
n, V = map(int, input().split(" "))
for i in range(n):
    l,w, h = map(int, input().split(" "))
    vi = l*w*h
    if vi > largest_box:
        largest_box = vi
print(largest_box - V)