from math import log2, sqrt

def algo(n, c, p):
    return (n*log2(n)**(c*sqrt(2)))/(p*10**9)

def tour(s, c, v):
    return s*(1 + 1/c)/v



n, p, s, v = map(float, input().split())

start = 0.0000001
end = 50
while abs(start - end) > 0.0000001:
    
    mid1 = start + (end-start)/3
    mid2 = end - (end - start)/3
    t1 = tour(s, mid1, v) + algo(n, mid1, p)
    t2 = tour(s, mid2, v) + algo(n, mid2, p)
    if t1 < t2:
        end = mid2
    else:
        start = mid1
            
print(algo(n, start, p) + tour(s, start, v), start)  