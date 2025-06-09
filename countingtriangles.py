# Algorithm based on this stack overflow post https://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect
# https://stackoverflow.com/users/68063/gareth-rees comment



def prod(x, y):
    return x[0] * y[1] - x[1] * y[0]
def check_intersect(first, sec):
    p = (first[0], first[1])
    r = (first[2] - first[0], first[3] - first[1])
    q = (sec[0], sec[1])
    s = (sec[2] - sec[0], sec[3] - sec[1])
    
    if prod(r, s) == 0 and prod((q[0] - p[0], q[1] - p[1]),r)== 0:
        return False
    elif prod(r,s ) == 0 and prod((q[0] - p[0], q[1] - p[1]),r) != 0:
        return False
    elif prod(r, s) != 0 :
        t = prod((q[0]-p[0], q[1] - p[1]), s)/prod(r, s)
        u = prod((q[0] - p[0], q[1] - p[1]),  r)/prod(r,s)
        if 0<=t<=1 and 0<=u<= 1:
            return True
        else:
            return False
    else:
        return False
    
while True:
    n = int(input())
    if n == 0:
        break
    points = []
    for i in range(n):
        x_1, y_1, x_2, y_2 = map(float, input().split(" "))
        points.append((x_1, y_1, x_2, y_2))
        
    res = 0
    for i in range(len(points) - 2):
        for j in range(i + 1, len(points) - 1):
            if check_intersect(points[i], points[j]):
                for k in range(j + 1, len(points)):
                    if check_intersect(points[j], points[k]) and check_intersect(points[i], points[k]):
                        res += 1
    print(res)