from math import dist, inf, sqrt


mindist = inf
mindistx = None
mindisty = None
r = int(input())
xstart = 0
xend = r+1
while xstart < xend:
    xmid = (xstart + xend)//2
    ystart = 0
    yend = r+1
    x_closest = inf
    y_closest = None
    while ystart < yend:
        ymid = (ystart + yend)//2
        if sqrt(xmid**2 + ymid**2) <= r:
            ystart = ymid + 1
        else:
            if sqrt(xmid**2 + ymid**2) < x_closest:
                x_closest = sqrt(xmid**2 + ymid**2)
                y_closest = ymid
            yend = ymid
        
    if x_closest <= r:
        xstart = xmid + 1
    else:
        if x_closest < mindist:
            mindist = sqrt(xmid**2 + yend**2)
            mindistx = xmid
            mindisty = y_closest
        xend = xmid
print(f"{mindistx} {mindisty}")