from math import floor



B, Br, Bs, A, As= map(int, input().split(" "))
k = floor((Br-B)*Bs/As + 1)
print(A + k)