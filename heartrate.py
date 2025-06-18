n = int(input())
for i in range(n):
    data = input().split(" ")
    b = int(data[0])
    p = float(data[1])
    bpm = (60 * b)/p
    ABPM = 60 / p
    print(f"{round(bpm - ABPM, 4)} {round(bpm, 4)} {round(bpm + ABPM, 4)}")