c = float(input())
# Have to satisfy x + y + z = 1
# So if z = 0, the max is x + y = 1
# If z = 1, the min is x+ y = 0
# So 0<= x+y<= 1
if c > 1:
    c = 1
print((c/2)*(c/2))