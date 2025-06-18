n, p = map(int, input().split())
alpha = 1
prob = p/(n+1)
while True:
    beta = ((alpha + 1) * ((n+alpha+1-p)/(n+alpha + 1)))/alpha
    if beta >= 1:
        prob *= beta
        alpha += 1
    else:
        break
print(prob)