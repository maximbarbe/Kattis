from math import inf
while True:
    try:
        n, m = map(int, input().split())
    except:
        exit()
    front= [*map(int, input().split())]
    back = [*map(int, input().split())]
    ratios = []
    for i in range(len(back)):
        for j in range(len(front)):
            ratios.append(back[i]/front[j])
    ratios.sort()
    maximum = -inf
    for i in range(len(ratios) - 1):
        spread = ratios[i + 1]/ratios[i]
        if spread > maximum:
            maximum = spread
            
    print(f"{round(maximum, 2):.2f}")