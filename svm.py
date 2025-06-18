def dot(w, x):
    return sum([w[i]*x[i] for i in range(len(w))])
    


n = int(input())
params = [*map(float, input().split())]
w = params[:-1]
b = params[-1]
norm = sum(map(lambda el:el**2, w))**0.5

while True:
    try:
        vals = [*map(float, input().split())]
        print((dot(w, vals) + b)/norm)
    except:
        exit()