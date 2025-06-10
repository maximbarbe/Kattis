s, n = map(int, input().split())
key = input().split()

def r(score):
    low = int(score)
    half = int(score) + 0.5
    high = int(score) + 1
    if abs(score - half) <= abs(low - score) and abs(score - half) <= abs(score - high):
        return str(half)
    else:
        return f"{round(score)}.0"


for i in range(n):
    name = input()
    res = input().split()
    score = 0
    for j in range(s):
        if res[j] == key[j]:
            score += 1
    print(f"{name}: {r(10* (score)/s)}")