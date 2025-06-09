from math import log
a, b, c = map(int, input().split(" "))
if a == 1:
    print("What an excellent example!")
elif c*log(b) == log(b) + log(c):
    print("What an excellent example!")
else:
    print("Oh look, a squirrel!")