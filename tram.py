n = int(input())

def distance(x0, y0, a):
    return abs(x0-y0+a)/(2**(1/2))



points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

start = -10**6
end = 10**6

while abs(end - start) > 0.0000005:
    m1 = start + (end - start)/3
    m2 = end - (end - start)/3
    
    f_m1 = sum(map(lambda el:el**2, [distance(points[i][0], points[i][1], m1) for i in range(len(points))]))
    f_m2 = sum(map(lambda el:el**2, [distance(points[i][0], points[i][1], m2) for i in range(len(points))]))
    
    if f_m1 < f_m2:
        end = m2
        
    elif f_m2 < f_m1:
        start = m1
    else:
        start = m1
        end = m2
    
    
    
print(start)