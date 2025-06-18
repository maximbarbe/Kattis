n = int(input())
score = 0
multiplier = 1
cur = 0
for i in range(n):
    note = int(input())
    if note == 0:
        if multiplier != 1:
            multiplier //= 2
        cur = 0
    else:
        cur += 1
        if cur == multiplier * 2:
            if multiplier < 8:
                multiplier *= 2
            cur = 0
        score += note * multiplier
print(score)