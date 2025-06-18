# Source for the formula: https://cs.uwaterloo.ca/journals/JIS/VOL24/Dukes/dukes3.pdf
# Page 9

def bins(n):
    res = []
    prev = 0
    i = 2 
    while prev != n:
        res.append((n - prev) % i)
        prev += res[-1]
        i +=  1
    return res
    
n = int(input())
for i in range(n):
    m, k = map(int, input().split(" "))
    res = bins(k)
    print(f"{m} {len(res)}")
    i = 0
    for i in range(0, len(res), 10):
        print(" ".join(map(str, res[i:i+10])))