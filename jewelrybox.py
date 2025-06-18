from math import sqrt

def get_h(x, y):
    top = (x+y) - sqrt(x**2 - x*y + y**2)
    return top/6

def get_volume(x,y, h):
    return (x - 2*h)*(y - 2*h)*h

n = int(input())
for i in range(n):
    x, y = map(int, input().split(" "))
    print(get_volume(x, y, get_h(x, y)))